<template>
  <el-container style="background-color: #E6EEFF">
    <el-header style="height: 200px">
      <el-row>
        <el-col :span="3">
          <router-link to="/">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
      </el-row>
      <h1 style="font-size: 40px;color:darkslategray; margin-top: 0px">欢迎来到cornerstone</h1>
    </el-header>
    <el-main style="height: 500px">

      <div class="big-box" style="background-color: #B8CDE6; color: darkslategray">
        <el-row>
          <h1>完善您的个人信息</h1>
        </el-row>
        <el-row>
          <el-avatar :src="qqInfo.data.figureurl_qq" :size="80"></el-avatar>
        </el-row>
        <el-row>
          <h3> {{qqInfo.data.nickname}}，欢迎您！</h3>
        </el-row>
      </div>
      <br>
      <div>

        <el-button type="info" plain round>开启新旅程</el-button>
      </div>
    </el-main>



    <div class="myfooter">

      <p style="color: grey">了解更多</p>

    </div>
  </el-container>

</template>



<script>

    import {Post,Get} from '../model/helper.js'

    export default {

        data() {
            return {
                session:"",
                qqInfo:[]
            }
        },

        methods:{
            getQQInfo(){
                Post('/api/user/auth').then(data=>{
                    this.qqInfo = data
                    console.log(data)
                })
            }
        },

        mounted() {
            this.getQQInfo()
        }
    }
</script>

<style>
  .circle_box{
    height: 80px;
    width: 80px;
    border-radius:50%;
    -webkit-border-radius:50%;
    -moz-border-radius:50%;
    margin-top: 15px;
  }
  .myfooter{
    position: fixed;
    bottom: 0px;
    z-index: 9999;
    width: 100%;
    background-color: #E6EEFF;

  }
  .big-box{
    border: 2px solid #C1D3E8;

  }
</style>
