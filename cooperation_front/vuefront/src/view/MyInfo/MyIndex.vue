<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
        <el-col :span="4">
          <router-link to="/mymodify" class="route-link">
            <i class="el-icon-edit" style="font-size: 25px"></i>
          </router-link>
        </el-col>
        <el-col :span="4" :offset="16" >
          <i class="el-icon-setting" style="font-size: 25px" @click="logout"></i>
        </el-col>
      </el-row>
      <el-row>
        <el-avatar :size="60" :src="userInfo.avatar"></el-avatar>
        <h1>{{userInfo.nickname}}</h1>
      </el-row>
    </el-header>

    <el-main>

      <el-row>
        <el-button  class="long-button" round @click="notready">我的计划</el-button>
      </el-row>
      <el-row>
        <el-button  class="long-button" round @click="gotoDocument">我的收藏</el-button>
      </el-row>
      <br>
      <el-row class="big-box">
        <el-col :span="8" style="margin-top: 10px" v-for="item in func" :key="item.name" >
          <router-link :to="item.path">
            <el-avatar style="background-color:#CBD6FE" shape="square" :size="60"><i :class="item.class" style="font-size: 50px"></i></el-avatar>
          </router-link>
          <p style="font-size: 13px; color:grey">{{item.name}}</p>
        </el-col>
      </el-row>
    </el-main>

    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import {getUserInfo} from "../../model/user";
    import {Post} from "../../model/helper";

    export default{
        components:{
            Footer,
        },
        data(){
            return {
                findData:"",
                func:[{'class':'el-icon-chat-line-square', 'name':'我的消息', 'path':'/mynotification'},
                      {'class':'el-icon-notebook-1', 'name':'我的好友', 'path':'/myfriend'},
                      {'class':'el-icon-pear', 'name':'我的宠物', 'path':'/mypet'},
                      {'class':'el-icon-s-opportunity', 'name':'关于我们1', 'path':'/about'},
                      {'class':'el-icon-s-opportunity', 'name':'关于我们2', 'path':'/about2'},
                      {'class':'el-icon-s-opportunity', 'name':'关于我们3', 'path':'/about3'},
                      ],
                userInfo:{},
                activeName: '推荐',
                search:"",

                plans:[{"_id": 1 ,"desc":"描述描述描述描述"},{"_id": 2 ,"desc":"描述描述描述描述"},{"_id": 3 ,"desc":"描述描述描述描述"},{"_id": 4 ,"desc":"描述描述描述描述"}]
            }
        },

        methods:{
            goto(){
              let path="/mynotification"
              console.log(path)
              this.$router.push(path)
            },

            gotoDocument(){
                let path="/mydocument"
                this.$router.push(path)
            },

            notready(){
                this.$message({
                    'message':'尚未开通此功能！',
                    'type': "warning"
                })
            },
            logout(){
                Post('/api/user/logout').then(data=>{
                    this.$router.push('/')
                    this.$message({
                        'message':"宁成功登出！",
                        'type': 'success'
                    })
                })
            }

        },


        mounted(){
            getUserInfo().then(data=>{
                if(data.code != 0){
                    alert("宁没有登录")
                    this.$router.push({path:'/'})
                }
                else{
                    this.userInfo = data.data
                }
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

  .route-link {
    text-decoration: none;
    color: black;
  }
</style>
