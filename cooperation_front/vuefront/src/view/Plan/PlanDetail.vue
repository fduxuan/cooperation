<template>
  <el-container>
    <el-header style="height:260px">
      <el-row style="display: flex;align-items: center">
        <el-col :span="3">
          <router-link to="/task">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
        <el-col :span="20">
          <h1>{{planInfo.desc}}</h1>
        </el-col>
      </el-row>

      <el-row>
        <el-image :src="test_1" style="height: 180px;"></el-image>
      </el-row>
    </el-header>
    <el-main>

      <el-dialog
        title="选择你的好友以及开始日期"
        :visible.sync="dialogVisible"
        width="90%"
        >
        <el-row>
          <el-date-picker
          v-model="startTime"
          type="date"
          format="yyyy 年 M 月 dd 日"
          value-format="yyyy-M-dd"
          placeholder="选择日期"
          :picker-options="pickerOptions">
          </el-date-picker>
        </el-row>
        <br>
        <el-row class="small-box" v-for="item in friends" :key="item._id" style="background-color: #fff">
          <el-col :span="6">
            <el-avatar :size="40" icon="el-icon-user-solid"></el-avatar>
          </el-col>
          <el-col :span="14">
            <el-row style="text-align: left">{{item.nickname}}</el-row>
          </el-col>
          <el-col :span="4">
            <el-button size="mini" round @click="createTask(item._id)">选择</el-button>
          </el-col>
        </el-row>
      </el-dialog>


      <el-row >
        <el-col :span="8"><h3>总时间:{{planInfo.days}}天</h3></el-col>
        <el-col :span="8" :offset="8"><h3>点赞:151人</h3></el-col>
      </el-row>
      <div style="margin: 30px">
        <el-row style="align-items: center; display: flex">
          <el-col :span="6">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6" @click="toLeft"></i>
          </el-col>
          <el-col :span="12">
            <h3 style="margin: 2px">第{{page+1}}天安排</h3>
          </el-col>
          <el-col :span="6">
            <i class="el-icon-arrow-right" style="font-size: 25px; color: #B8CDE6" @click="toRight"></i>
          </el-col>
        </el-row>
        <br>
        <div v-for="(value, key) in planInfo.tasks[page]" :key="key">
          <el-row class="row-text-left">
            <h4 style="margin: 5px">{{key}}</h4>
          </el-row>
          <el-row class="row-text-left">
            <el-col :offset="2">
              {{value}}
            </el-col>
          </el-row>
        </div>
        <br>
        <div>
          <el-row>
            <el-col :span="6">
              <el-button style="background-color: #C1D3E8" @click="dialogVisible = true">发起任务</el-button>
            </el-col>
            <el-col :span="6" :offset="8">
              <el-button style="background-color: #C1D3E8" @click="addToDocument">加入收藏</el-button>
            </el-col>
          </el-row>
        </div>
      </div>
      <el-divider></el-divider>

      <div>
        <el-row style="text-align: left">
          <el-col :span="8">
            <h3 style="margin-top: 0px">热门评论:</h3>
          </el-col>
          <el-col :span="8" :offset="8">
            <h5 style="margin-top: 4px; color: grey" @click="goto">查看更多</h5>
          </el-col>
        </el-row>
        <div class="big-box" v-for="item in comments" :key="item._id" style="text-align: left">
            &nbsp;{{item.sender}}:
          <el-row>
            <el-col :span="20" :offset="3">{{item.message}}</el-col>
          </el-row>
        </div>
      </div>
    </el-main>

    <br>
    <br>
    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import test_1 from "../../assets/test_1.jpg"
    import {Post} from "../../model/helper";
    import {getUserInfo} from "../../model/user";

    export default{
        components:{
            Footer,
        },
        data(){
            return {

                test_1: test_1,
                search: "",
                activeName:"今日未完成",
                score:["10", "10"],
                task_time:{'whole': 60, 'current': 15},
                checked: false,
                pid: this.$route.params.pid,
                planInfo: {},
                page: 0,
                count: 0,
                comments:[],
                dialogVisible: false,
                startTime:"",
                friends: [],
                pickerOptions: {
                    disabledDate(time) {
                        return time.getTime() <= Date.now();
                    },
                },
                user:{}
            }
        },

        methods:{
            handleClick(tab) {
                console.log(tab.name);
            },

            getPlan(){
                Post('/api/plan/find', {filter: {_id: this.pid}}).then(data =>{
                    this.planInfo = data.data[0]
                    console.log(data)
                    this.count = this.planInfo.days

                })
            },

            getComment(){
                Post('/api/notification/find', {filter: {plan_id : this.pid}}).then(data =>{
                    this.comments = data.data
                })
            },

            toLeft(){
              if(this.page > 0){
                  this.page = this.page - 1
              }
            },

            toRight(){
              if(this.page < this.count-1){
                  this.page = this.page+1
              }
            },

            createTask(uid){
                //时间不可选之前的，自动format为2018-1-11
                if(this.startTime == ""){
                    this.$message({
                        message: '请选择开始日期',
                        type: 'warning'
                    });
                    return;
                }
                let date = new Date()

                let date_now = date.getFullYear()+'-'+ (date .getMonth()+1) + '-' + date.getDate()
                console.log(date_now)
                Post('/api/task/create', {uid: uid, pid:this.pid, start: this.startTime}).then(data=>{
                    console.log(data)
                    this.dialogVisible=false
                    if(data.code != 0 ){
                        this.$message({
                            'message': "您已经有此任务！",
                            'type': "warning"
                        })
                    }
                    else{
                        this.$message({
                            'message': "创建成功！",
                            'type': "success"
                        })
                        let notification={}
                        notification['sender'] = this.user._id
                        notification['receiver'] = uid
                        notification['message'] = this.user.nickname+" 邀请你加入了计划"
                        let date = new Date()
                        notification['time'] = date.getFullYear() +"-"+ (date.getMonth()+1) + "-"+ date.getDate()+"-"+date.getHours()+":"+date.getMinutes()
                        notification['is_read'] = false
                        notification['type']='plan'
                        Post('/api/notification/create', notification).then(data=>{
                            console.log(data)
                        })
                    }

                })

            },
            getFriend(){
                getUserInfo().then(data=>{
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
            },
            addToDocument(){
                let document = []
                if(this.user['document']!=undefined){
                    document = this.user['document']
                }
                if(document.indexOf(this.pid)>=0){
                    this.$message({
                        "message": "宁已收藏！",
                        'type': "warning"
                    })
                }
                else{
                    document.push(this.pid)
                    this.user['document'] = document
                    Post('/api/user/' +this.user['_id']+'/update', this.user).then(data =>{
                        this.$message({
                            'message':"收藏成功！",
                            'type': "success"
                        })
                    })


                }
            },

            goto(){
                this.$message({
                    'message':'作者累了(^_^),写不动了',
                    'type':"warning"
                })
            }
        },

        mounted(){
            this.getPlan()
            this.getComment()
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

  .small-box-2{
    background-color: #B8CDE6;
    display: flex;
    align-items: center;
  }
  .row-text-left{
    text-align: left;
    height: 40px;
  }
  .big-box{
    border: 2px solid #C1D3E8;
  }
  .small-box{
    background-color: #B8CDE6;
    margin: 10px;
    height: 50px;
    display: flex;
    align-items: center;
  }
</style>
