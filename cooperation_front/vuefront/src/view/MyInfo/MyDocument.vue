<template>
  <el-container>
    <el-header style="height:100px">
      <el-row>
        <el-col :span="3">
          <router-link to="/myindex">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
      </el-row>
      <el-row>
        <h1>我的收藏</h1>
        <el-divider></el-divider>
      </el-row>

    </el-header>
    <el-main>
      <div class="big-box" v-if="tasks.length!=0">

        <el-row v-for="item in tasks" :key="item._id" style="margin-top: 5px; align-items: center; display: flex; text-align: center" >

            <el-col :span="8" :offset="1">
              <router-link :to="{ name: 'plandetail', params: { pid: item._id } }" class="route-link" >
                <el-image :src="test_1"></el-image>
              </router-link>
            </el-col>

            <el-col :span="12">
              <router-link :to="{ name: 'plandetail', params: { pid: item._id } }" class="route-link" >
                <p>{{item.desc}}</p>
              </router-link>
            </el-col>
            <el-col :span="4">
              <i class="el-icon-delete" style="font-size: 25px" @click="removeDocument(item._id)"></i>
            </el-col>

        </el-row>

      </div>
      <div class="big-box" v-else>
        <el-row >
          宁还没有收藏哦～快去添加吧～
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
                tasks:[],
                test_1:test_1,
                user:{}
            }
        },

        methods:{

            async getTasks(){
                let user = await getUserInfo()
                if(user.code != 0){
                    alert("宁没有登录")
                    this.$router.push({path:'/'})
                }
                else{
                    this.user= user.data
                    console.log(user.data._id)
                    let document = []
                    if(user.data['document']!=undefined){
                        document = user.data['document']
                    }
                    console.log(document)
                    let task1 = await Post('/api/plan/find', {filter:{"_id": {"$in": document}}})
                    console.log(task1)
                    this.tasks = task1.data
                }

            },
            removeDocument(tid){
                let document = this.user['document']
                console.log(document)
                let i = document.indexOf(document)
                document.splice(i)
                Post('/api/user/'+this.user._id+'/update', this.user).then(data =>{
                    this.$message({
                        'message':'成功取消！',
                        'type': "success"
                    })
                    this.getTasks()
                })

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
