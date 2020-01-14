<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
          <h1 style="margin-top: 0px">我的好友</h1>
      </el-row>
      <el-row>
        <el-col :span="16">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane  v-for="item in tags" :key="item"  :label="item" :name="item" style="width: 100px">
              <el-input size="small" v-model="search" placeholder="请输入搜索内容"></el-input>
            </el-tab-pane>
          </el-tabs>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-button round style="background-color: #C1D3E8" @click="dialogVisible = true">添加好友</el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>

      <el-dialog
        title="输入用户email或者昵称"
        :visible.sync="dialogVisible"
        width="90%"
        >
        <el-row style="display: flex; align-items: center">
          <el-col :span="18">
            <el-input size="small" v-model="search2" placeholder="请输入搜索内容"></el-input>
          </el-col>
          <el-col :span="4" :offset="1">
            <el-button size="mini" round @click="findNew">搜索</el-button>
          </el-col>
        </el-row>
        <el-row class="small-box" v-for="item in searchusers" :key="item._id" style="background-color: #fff">
          <el-col :span="6">
            <el-avatar :size="40" icon="el-icon-user-solid"></el-avatar>
          </el-col>
          <el-col :span="14">
            <el-row style="text-align: left">{{item.nickname}}</el-row>
          </el-col>
          <el-col :span="4">
            <el-button size="mini" round @click="addFriend(item._id, item.nickname)">添加</el-button>
          </el-col>
        </el-row>
        <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>


      <div class="big-box">
        <el-row class="small-box" v-for="item in friends" :key="item._id">
          <el-col :span="6">
            <el-avatar :size="40" icon="el-icon-user-solid"></el-avatar>
          </el-col>
          <el-col :span="14">
            <el-row style="text-align: left">{{item.nickname}}</el-row>
            <el-row style="text-align: left">{{item.email}}</el-row>
          </el-col>

<!--          <el-col :span="2" >-->
<!--            <el-badge :value="1" ></el-badge>-->
<!--          </el-col>-->
        </el-row>
      </div>
    </el-main>


    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import {Post} from "../../model/helper";
    import {getUserInfo} from "../../model/user";

    export default{
        components:{
            Footer,
        },
        data(){
            return {
                tags:['我的关注', '新的好友'],
                activeName:'我的关注',
                notifications:[
                    {'_id':1, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                    {'_id':2, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                    {'_id':3, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                    {'_id':4, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                    {'_id':5, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                    {'_id':6, 'name':"nickname", 'time':'2019-10-22 8:30', 'read':'false'},
                ],
                search: "",
                dialogVisible: false,
                search2: "",
                searchusers:[],
                friends: [],
                user:{}
            }
        },

        methods:{
            handleClick(tab) {
                console.log(tab.name);
            },

            findNew(){
                if(this.search2 == ""){
                    return
                }
                let data = this.search2
                let query = {"$or": [{"nickname":{"$regex": data}}, {"email": data}]}
                Post('/api/user/find', {filter: query}).then(data=>{
                    console.log(data)
                    this.searchusers = data.data
                })
            },

            addFriend(uid, nickname){
                Post('/api/user/add/friend', {uid: uid}).then(data=>{
                    if(data.code != 0){
                        this.$message({
                            'message': data.error,
                            'type':"warning"
                        })

                    }
                    let notification={}
                    notification['sender'] = this.user._id
                    notification['receiver'] = uid
                    notification['message'] = this.user.nickname+" 添加你为好友"
                    let date = new Date()
                    notification['time'] = date.getFullYear() +"-"+ (date.getMonth()+1) + "-"+ date.getDate()+"-"+date.getHours()+":"+date.getMinutes()
                    notification['is_read'] = false
                    notification['type']='friend'
                    Post('/api/notification/create', notification).then(data=>{
                        console.log(data)
                    })
                })
            },

            getFriend(){
                getUserInfo().then(data=>{
                    if(data.code != 0){
                        alert("宁没有登录")
                        this.$router.push({path:'/'})
                        return
                    }
                    this.user=data.data
                    let friend = data.data['friend']
                    if(friend == undefined){
                        friend = []
                    }
                    Post('/api/user/find', {filter: {"_id": {"$in": friend}}}).then(data=>{
                        console.log(data)
                        this.friends = data.data
                    })
                })
            }
        },

        mounted(){
            this.getFriend()
        }
    }

</script>

<style>
  .long-button{
    width: 100%;
    background-color: #B8CDE6;
    height: 50px;
  }
  .big-box{
    border: 2px solid #C1D3E8;
  }
  .message{
    margin-top: 10px;
    margin-right: 40px;
  }
  .small-box{
    background-color: #B8CDE6;
    margin: 10px;
    height: 50px;
    display: flex;
    align-items: center;
  }
</style>
