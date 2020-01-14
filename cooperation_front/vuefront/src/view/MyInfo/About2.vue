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
        <h1>感悟</h1>
        <el-divider></el-divider>
      </el-row>

    </el-header>
    <el-main>

      <div class="big-box" v-if="tasks.length!=0">

        <el-row v-for="item in tasks" :key="item" style="margin-top: 15px; align-items: center; display: flex; text-align: left; font-size: 20px" >
          <el-col :offset="3">{{item}}</el-col>


        </el-row>

      </div>
<br><br>

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
                    "cordova打包，为什么会找不到android sdk ！@#*（Y*&！@#",
                    "为什么js数字的排序也是字符串的！！！",
                    "UI越调越丑，换了n种颜色死心了",
                    "等等，这个私信是不是要ws？需求去掉去掉",
                    "怎么这页面就写不完了呢？？？",
                    "当初夸下的海口是现在脑子里进的水"
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
