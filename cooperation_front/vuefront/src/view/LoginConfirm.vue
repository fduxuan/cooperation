<template>
  <el-container style="background-color: #E6EEFF">
    <el-header style="height: 160px">
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
      <div v-if="flag==0">
        <el-row>
          <el-col style="text-align: left"><h4 style="margin: 5px;">绑定您的邮箱地址:</h4></el-col>
        </el-row>
        <el-row style="display: flex; align-items: center; ">
          <el-col :span="16">
            <el-input v-model="email_add" size="medium" placeholder="请输入您的邮箱"></el-input>
          </el-col>
          <el-col :span="4"> <el-button type="info" plain round @click="sendEmail">获取验证码</el-button></el-col>
        </el-row>

      </div>
      <div v-if="flag==1">
        <el-row>
          <el-col style="text-align: left"><h4 style="margin: 5px;">{{email_add}}:</h4></el-col>
        </el-row>
        <el-row style="display: flex; align-items: center">
          <el-col :span="12"><h4>请输入验证码:</h4></el-col>
          <el-col :span="12">
            <el-input v-model="check_code" size="medium" placeholder="验证码"></el-input>
          </el-col>
        </el-row>
        <el-button type="info" plain round @click="confirm">确认登录</el-button>
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
                qqInfo:[],
                email_add:"",
                flag: 0,
                check_code:"",
                real_check_code:"",
                access_token:this.$route.query.access_token,
                userId:this.$route.query.userId,

            }
        },

        methods:{
            checkRegister(){
                Post('/api/user/find', {filter:{"access_token": this.access_token}}).then(data=>{
                    let res = data.data[0]
                    console.log(data)
                    if(res!=undefined){
                        let loginData = {
                            "_id": res._id,
                            "nickname": res.nickname
                        }

                        Post('/api/user/login',loginData).then(data=>{
                            this.$router.push({path:'/square'})
                        })

                    }
                })
            },


            getQQInfo(){
                Post('/api/user/auth', {access_token: this.access_token, userId: this.userId}).then(data=>{
                    this.qqInfo = data
                    console.log(data)
                })
            },

            sendEmail(){
                let data = {"email": this.email_add, "nickname":this.qqInfo.data.nickname}

                Post('/api/user/email', data).then(data =>{
                    console.log(data)
                    this.real_check_code = data.data

                })
                this.flag=1
            },

            confirm(){
                if(this.check_code != this.real_check_code){
                    this.$message.error('验证码错误！');

                }
                else{
                    let registerData = {
                        "email": this.email_add,
                        "access_token":"F6D42A2437E562738B44459B47334D21",
                        "nickname":this.qqInfo.data.nickname,
                        "avatar": this.qqInfo.data.figureurl_qq,
                        "sex": this.qqInfo.data.sex,
                        "pet": 0,
                        "score": 0,
                        'birthday': "",
                        'desc':''
                    }
                    Post("/api/user/register",registerData).then(data=>{
                        console.log(data)
                        if(data.code!=0){
                            this.$message({
                                'message': data.error,
                                'type': "warning"
                            })
                            return
                        }
                        let loginData = {
                            "_id": this.email_add,
                            "nickname": this.qqInfo.data.nickname,
                        }
                        Post('/api/user/login',loginData).then(data=>{
                            this.$router.push({path:'/square'})
                        })
                    })
                }



            }
        },


        mounted() {
            console.log(this.$route.query)
            this.checkRegister()
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
