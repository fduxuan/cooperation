<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
        <el-badge :value="num" class="message">
          <h1 style="margin-top: 0px">我的消息</h1>
        </el-badge>
      </el-row>
      <el-row>
        <el-col :span="16">
          <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane  v-for="item in tags" :key="item"  :label="item" :name="item" style="width: 100px">{{item}}</el-tab-pane>
          </el-tabs>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-button round style="background-color: #C1D3E8">全部已读</el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <div class="big-box" v-if="notifications.length>0">
        <el-row class="small-box" v-for="item in notifications" :key="item._id">
          <el-col :span="6">
            <el-avatar :size="40" icon="el-icon-user-solid"></el-avatar>
          </el-col>
          <el-col :span="14">
            <el-row style="text-align: left">{{item.message}}</el-row>
            <el-row style="text-align: left">{{item.time}}</el-row>
          </el-col>

          <el-col :span="2" >
            <i class="el-icon-message"></i>
          </el-col>
        </el-row>
      </div>
      <div class="big-box" v-else>
        <el-row>
          暂无消息
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
                tags:['关于计划', '关于好友'],
                activeName:'关于计划',
                notifications:[
                    ],
                num:0
            }
        },

        methods:{
            handleClick(tab) {
                console.log(tab.name);
                let query = {}
                if(tab.name=='关于好友'){
                    query={"type": "friend"}
                }
                else{
                    query = {'type': 'plan'}
                }
                this.getNotifications(query)
            },

            async getNotifications(query={}){
                let user = await getUserInfo()
                let notifications = await Post('/api/notification/find', {filter:{"$and":[{receiver: user.data._id}, query]}})
                console.log(notifications)
                this.notifications = notifications.data
            }
        },

        mounted(){
            this.getNotifications()
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
