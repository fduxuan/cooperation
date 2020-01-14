<template>
  <el-container>
    <el-header style="height:250px">
      <el-row style="display: flex;align-items: center">
        <el-col :span="3">
          <router-link to="/task">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
        <el-col :span="20">
          <h1>{{taskInfo.desc}}</h1>
        </el-col>
      </el-row>

      <el-row>
        <el-image :src="test_1" style="height: 180px;"></el-image>
      </el-row>
    </el-header>
    <el-main>
      <div class="big-box">
        <el-row style="text-align: left;">
          <el-col :span="12" :offset="1"><p>我的累计积分:{{taskInfo.score[uid]}}</p></el-col>
          <el-col :span="10"><p>每日完成得分: 5</p></el-col>
        </el-row>
        <el-row class="row-text-left">
          <el-col :span="12" :offset="1"><p>当前:{{current}}</p></el-col>
          <el-col :span="10"><p>总时间:{{taskInfo.days}}天</p></el-col>
        </el-row>
      </div>

      <div style="margin: 30px">

        <h3 style="margin: 2px">第{{diff}}日安排</h3>

        <div v-for="(value, key) in taskInfo.tasks[diff-1]" :key="key">
          <el-row class="row-text-left">
            <h4 style="margin: 5px">{{key}}</h4>
          </el-row>

          <el-row class="row-text-left">
            <el-col :offset="1">
              {{value}}
            </el-col>
          </el-row>
        </div>

        <el-button style="background-color: #B8CDE6" @click="confirmFinish">{{button_name}}</el-button>
        <br>
        <br>
        <br>
        <el-row style="font-size: 13px">
          <el-col :span="10">
            <router-link class="route-link" :to="{ name: 'plandetail', params: { pid: taskInfo.pid }}">
              关于此计划
            </router-link>
          </el-col>

          <el-col :span="12" :offset="2">
            {{myfinish}}
          </el-col>
        </el-row>
      </div>


    </el-main>


    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import test_1 from "../../assets/test_1.jpg"
    import {getUserInfo} from "../../model/user";
    import {Post} from "../../model/helper";

    export default{
        components:{
            Footer,
        },
        data(){
            return {
                tid: this.$route.params.tid,
                test_1: test_1,
                search: "",
                activeName:"今日未完成",
                score:["10", "10"],
                task_time:{'whole': 60, 'current': 15},
                checked: false,
                count: 0,
                taskInfo:{},
                user:{},
                current:"",
                diff: 0,
                uid: "",
                friend_uid: "",
                button_name:"确认对方已完成",
                myfinish:"宁今日尚未完成"
            }
        },

        methods:{
            handleClick(tab) {
                console.log(tab.name);
            },

            async getTask(){
                let user = await getUserInfo()
                if(user.code != 0){
                    alert("宁没有登录")
                    this.$router.push({path:'/'})
                }
                else {
                    this.user = user.data

                    let taskInfo = await Post('/api/task/find', {filter: {_id: this.tid}})

                    this.taskInfo = taskInfo.data[0]

                    if(user._id == this.taskInfo.uid1){ this.uid = 'uid1'; this.friend_uid='uid2'}
                    else{this.uid='uid2'; this.friend_uid='uid1'}

                    let date = new Date()
                    let date_now = date.getFullYear()+'-'+ (date .getMonth()+1) + '-' + date.getDate()
                    let diff = this.dateDiff(date_now, this.taskInfo.start)
                    let length = this.taskInfo.days

                    if(diff < 0){
                        this.current = "还有" + Math.abs(diff) + "天开始"
                        this.diff = 1
                        this.button_name="尚未开始"
                    }
                    else if (diff >= length){
                        this.current = "已结束"
                        this.diff = length-1
                        this.button_name="已结束"
                    }
                    else{
                        this.current = diff + 1
                        this.diff = diff + 1
                        let finish = this.taskInfo.finish
                        if(finish[this.friend_uid][diff-1]!=0){
                            this.button_name="对方已完成"
                        }
                        if(finish[this.uid][diff-1] != 0){
                            this.myfinish="宁已完成"
                        }
                    }
                }
            },

            dateDiff(sDate1, sDate2) { //sDate1和sDate2是2019-3-12格式

                let aDate, oDate1, oDate2, iDays
                aDate = sDate1.split("-")
                oDate1 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0]) //转换为9-25-2017格式
                aDate = sDate2.split("-")
                oDate2 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0])
                iDays = parseInt((oDate1 - oDate2) / 1000 / 60 / 60 / 24) //把相差的毫秒数转换为天数
                return iDays
            },

            confirmFinish(){
                if(this.button_name=="确认对方已完成"){
                    this.taskInfo.finish[this.friend_uid][this.diff-1] = 1
                    this.taskInfo[this.friend_uid] += 5
                    Post('/api/task/'+this.taskInfo._id+ '/update', this.taskInfo).then(data=>{
                        console.log(data)
                        this.button_name = "对方已完成"
                    })
                }
                else{
                    this.$message({
                        'message': "当前不可进行此操作！",
                        'type': "warning"
                    })
                }
            }

        },

        mounted(){
            this.getTask()
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
  .route-link {
    text-decoration: none;
    color: black;
  }
</style>
