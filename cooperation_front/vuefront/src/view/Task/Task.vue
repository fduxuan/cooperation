<template>
  <el-container>
    <el-header style="height:200px">
      <el-row>
        <h1>我的当前任务</h1>
      </el-row>

      <el-row class="small-box-2">
        <el-col :span="18" >
          <el-input size="small" v-model="search" placeholder="请输入搜索内容"></el-input>
        </el-col>
        <el-col :span="2" :offset="2">
          <i style="font-size:20px" class="el-icon-search"></i>
        </el-col>
      </el-row>
      <br>
      <el-row>
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="准备中" name="first"></el-tab-pane>
          <el-tab-pane label="进行中" name="second"></el-tab-pane>
          <el-tab-pane label="历史" name="third"></el-tab-pane>
        </el-tabs>
      </el-row>
    </el-header>
    <el-main>
      <div class="big-box" v-if="tasks.length!=0">

        <el-row v-for="item in tasks" :key="item._id" style="margin-top: 5px;" >
          <router-link :to="{ name: 'taskdetail', params: { tid: item._id } }" class="route-link" >
          <el-col :span="8" :offset="1">
            <el-image :src="test_1"></el-image>
          </el-col>
          <el-col :span="15">
            <p>{{item.desc}}</p>
          </el-col>
          </router-link>
        </el-row>

      </div>
      <div class="big-box" v-else>
        <el-row >
          暂无数据
        </el-row>


      </div>

      <br>
    </el-main>


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
                plans:[{"_id": 1 ,"desc":"描述描述描述描述"},{"_id": 2 ,"desc":"描述描述描述描述"},{"_id": 3 ,"desc":"描述描述描述描述"},{"_id": 4 ,"desc":"描述描述描述描述"},
                    {"_id": 5 ,"desc":"描述描述描述描述"}],
                test_1:test_1,
                search: "",
                activeName:"今日未完成",
                tasks:[],
                task_todo:[],
                task_progress:[],
                task_done:[]
            }
        },

        methods:{
            handleClick(tab) {
                console.log(tab.name);
                this.search=""
                if(tab.name == "first"){
                    this.tasks = this.task_todo
                }
                else if (tab.name == "second"){
                    this.tasks = this.task_progress
                }
                else{
                    this.tasks = this.task_done
                }
            },

            async getTasks(query=undefined){
                let user = await getUserInfo()
                if(user.code != 0){
                    alert("宁没有登录")
                    this.$router.push({path:'/'})
                }
                else{
                    console.log(user._id)
                    let task1 = await Post('/api/task/find', {filter:{$or:[{uid1: user.data.uid1}, {uid2: user.data.uid2}], query}})
                    console.log(task1)
                    this.split_tasks(task1.data)
                    this.tasks = this.task_todo
                    console.log(this.tasks)
                }

            },

            split_tasks(tasks){
                let date = new Date()
                for(let i = 0; i<tasks.length; i++){
                    let task = tasks[i]
                    let length = task.days
                    let start = task.start
                    let date_now = date.getFullYear()+'-'+ (date .getMonth()+1) + '-' + date.getDate()

                    let diff = this.dateDiff(date_now, start)

                    if(diff<0){
                        //尚未开始
                        this.task_todo.push(task)
                    }
                    else if(diff >= length){
                        this.task_done.push(task)
                    }
                    else{
                        this.task_progress.push(task)
                    }

                }

            },
            dateDiff(sDate1, sDate2) { //sDate1和sDate2是2019-3-12格式

                var aDate, oDate1, oDate2, iDays
                aDate = sDate1.split("-")
                oDate1 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0]) //转换为9-25-2017格式
                aDate = sDate2.split("-")
                oDate2 = new Date(aDate[1] + '-' + aDate[2] + '-' + aDate[0])
                iDays = parseInt((oDate1 - oDate2) / 1000 / 60 / 60 / 24) //把相差的毫秒数转换为天数
                return iDays
            }
        },

        mounted(){
            this.getTasks()

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

  .small-box-2{
    background-color: #B8CDE6;
    display: flex;
    align-items: center;
  }
  .route-link {
    text-decoration: none;
    color: black;
  }
</style>
