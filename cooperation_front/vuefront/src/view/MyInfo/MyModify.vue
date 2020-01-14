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
        <el-avatar :size="70" :src="userInfo.avatar"></el-avatar>

        <p>{{userInfo.desc}}</p>
      </el-row>
    </el-header>
    <el-main>
      <div class="big-box">
        <el-row class="small-box">
          <el-col :span="6" :offset="1" style="text-align: left">
            <i class="el-icon-user" ></i>昵称
          </el-col>
          <el-col :span="16" style="text-align: right">
            {{userInfo.nickname}}
          </el-col>
          <el-col :span="2">
            <router-link :to="{path:'/mymodifydetail', query:{flag:'nickname'}}">
              <i class="el-icon-arrow-right" style="color:#A8A3D4;font-weight: bold"></i>
            </router-link>r
          </el-col>
        </el-row>

        <el-row class="small-box">
          <el-col :span="6" :offset="1" style="text-align: left">
            <i class="el-icon-male" ></i>&nbsp;性别
          </el-col>
          <el-col :span="16" style="text-align: right">
            {{userInfo.sex}}
          </el-col>
          <el-col :span="2">
            <router-link :to="{path:'/mymodifydetail', query:{flag:'sex'}}">
              <i class="el-icon-arrow-right" style="color:#A8A3D4;font-weight: bold"></i>
            </router-link>
          </el-col>
        </el-row>

        <el-row class="small-box">
          <el-col :span="6">
            <i class="el-icon-chicken" :offset="1" style="text-align: left"></i>&nbsp;生日
          </el-col>
          <el-col :span="16" style="text-align: right">
            {{info.birthday}}
          </el-col>
          <el-col :span="2">
            <router-link :to="{path:'/mymodifydetail', query:{flag:'birthday'}}">
              <i class="el-icon-arrow-right" style="color:#A8A3D4;font-weight: bold"></i>
            </router-link>
          </el-col>
        </el-row>

        <el-row class="small-box">
          <el-col :span="6">
            <i class="el-icon-star-off" :offset="1" style="text-align: left"></i>&nbsp;简介
          </el-col>
          <el-col :span="16" style="text-align: right">
            我的个人简介
          </el-col>
          <el-col :span="2">
            <router-link :to="{path:'/mymodifydetail', query:{flag:'desc'}}">
              <i class="el-icon-arrow-right" style="color:#A8A3D4;font-weight: bold"></i>
            </router-link>
          </el-col>
        </el-row>

        <el-row class="small-box">
          <el-col :span="6" :offset="1" style="text-align: left">
            <i class="el-icon-postcard" :offset="1" style="text-align: left"></i>&nbsp;email
          </el-col>
          <el-col :span="16" style="text-align: right">
            {{userInfo.email}}
          </el-col>
          <el-col :span="2">
            <i class="el-icon-arrow-right" style="color:#A8A3D4;font-weight: bold"></i>
          </el-col>
        </el-row>

      </div>
    </el-main>


    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import {getUserInfo} from "../../model/user";

    export default{
        components:{

            Footer,
        },
        data(){
            return {
                info:{"name": "nickname", "sex": "女", "birthday":"2010-04-01", "des":"我的个人简介",
                      '_id':"12342423"},
                userInfo:{}
            }
        },

        methods:{
            gotoModify(){

            }
        },

        mounted(){
          getUserInfo().then(data=>{
              this.userInfo=data.data
          })
        }
    }

</script>

<style>
  .long-button{
    width: 100%;
    background-color: #C1D3E8;
    height: 50px;
  }
  .big-box{
    border: 2px solid #C1D3E8;

  }
  .small-box{
    background-color: #B8CDE6;
    margin: 10px;
    height: 50px;
    align-items: center;
    display: flex;
  }
</style>
