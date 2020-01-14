<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
        <el-col :span="3">
          <router-link to="/myindex">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
        <h1>技术栈</h1>
        <el-divider></el-divider>
      </el-row>

    </el-header>
    <el-main>

      <div class="big-box" v-if="tasks.length!=0">

        <el-row v-for="item in tasks" :key="item" style="margin-top: 15px; align-items: center; display: flex; text-align: left; font-size: 20px" >
          <el-col :offset="3">{{item}}</el-col>


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
                tasks:[
                    "1. 后端 sanic",
                    "2. 前端 vue+cordova",
                    "3. qq 第三方接入",
                    "4. UI element + ali icon库",
                    "5. 部署 docker",
                    "6. 数据库 mongodb + redis"
                ],
                test_1:test_1,
                user:{}
            }
        },

        methods:{




        },

        mounted(){


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
