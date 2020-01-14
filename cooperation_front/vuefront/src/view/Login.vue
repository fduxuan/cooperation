<template>
  <el-container style="background-color: #E6EEFF">
    <el-header style="height: 200px">
      <h1 style="font-size: 40px;color:darkslategray">欢迎来到cornerstone</h1>
    </el-header>
    <el-main style="height: 500px">
      <el-row>
        <img src="../assets/logo.png">
      </el-row>
    </el-main>

    <div class="myfooter">
      <el-row justify="space-around">
        <el-col :span="6" :offset="4" >
<!--          <router-link :to="{path:'/loginconfirm', query:{access_token: access_token, userid: userid}}">-->
            <i class="iconfont icon-qq" @click="login2"></i>
<!--          </router-link>-->
        </el-col>
        <el-col :span="6" :offset="4">
          <i class="iconfont icon-weixin" @click="login"></i>
        </el-col>
      </el-row>
      <el-row>
        <p style="color: grey">了解更多</p>
      </el-row>
    </div>
  </el-container>

</template>



<script>

import {Post,Get} from '../model/helper.js'

export default {

    data() {
        return {
            session:"",
            access_token:"F6D42A2437E562738B44459B47334D21",
            userId: "B3E34A351CD1B778D04CAB33C05B5541"

        }
    },

    methods:{
        login(){



            var args = {};
            args.client = QQSDK.ClientType.QQ;//QQSDK.ClientType.QQ,QQSDK.ClientType.TIM;
            let that = this
            res = QQSDK.ssoLogin(result=> {
                //alert('token is ' + result.access_token, 'userid is ' + result.userid, );
                //alert('userid is ' + result.userid);
                //alert('expires_time is ' + new Date(parseInt(result.expires_time)) + ' TimeStamp is ' + result.expires_time);
                //var url = 'https://graph.qq.com/user/get_user_info?access_token=' + result.access_token + '&oauth_consumer_key=' + '101834891' + '&openid=' + result.userid;
                //this.access_token = result.access_token

                that.$router.push({path:'/loginconfirm',
                    query: {
                        'access_token': result.access_token,
                        'userId': result.userid
                    }
                })
            }, function (failReason) {
                alert(failReason);
            }, args);


        },

        login2(){
            this.$router.push({path:'/loginconfirm',
                query: {
                    'access_token': this.access_token,
                    'userId': this.userId
                }
            })
        }
    },
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
</style>
