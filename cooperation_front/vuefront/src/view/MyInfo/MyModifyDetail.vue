<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
        <el-col :span="3">
          <router-link to="/mymodify">
            <i class="el-icon-arrow-left" style="font-size: 25px; color: #B8CDE6"></i>
          </router-link>
        </el-col>
        <el-col :span="4" :offset="16" >
          <i class="el-icon-check" style="font-size: 25px" @click="update"></i>
        </el-col>
      </el-row>

      <el-row>



        <h1>修改个人信息</h1>
      </el-row>
    </el-header>
    <el-main>
      <el-row class="small-box" v-if="flag=='sex'">
        <el-col :span="6" :offset="1" style="text-align: left">
          <i class="el-icon-male" ></i>&nbsp;性别
        </el-col>
        <el-col :span="16" style="text-align: right">
          <el-select v-model="sex_change" placeholder="请选择">
            <el-option
              v-for="item in sexs"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-col>
      </el-row>

      <el-row class="small-box" v-if="flag=='nickname'">
        <el-col :span="6" :offset="1" style="text-align: left">
          <i class="el-icon-user" ></i>昵称
        </el-col>
        <el-col :span="16" style="text-align: right">
          <el-input v-model="nickname_change" placeholder="请输入昵称">

          </el-input>
        </el-col>
      </el-row>

      <el-row class="small-box" v-if="flag=='birthday'">
        <el-col :span="6">
          <i class="el-icon-chicken" :offset="1" style="text-align: left"></i>&nbsp;生日
        </el-col>
        <el-col :span="16" style="text-align: right">
          <el-date-picker
            v-model="birthday_change"
            type="date"
            placeholder="选择日期"
            format="yyyy 年 MM 月 dd 日"
            value-format="yyyy-MM-dd">
          </el-date-picker>
        </el-col>
      </el-row>

        <el-row class="small-box" v-if="flag=='desc'">
          <el-col :span="6">
            <i class="el-icon-star-off" :offset="1" style="text-align: left"></i>&nbsp;简介
          </el-col>
          <el-col :span="16" style="text-align: right">
            我的个人简介
          </el-col>

        </el-row>

      <br>
      <el-row class="small-box" v-if="flag=='desc'">
      <el-input
        type="textarea"
        :rows="4"
        placeholder="请输入内容"
        v-model="textarea">
      </el-input>
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
                flag: this.$route.query.flag,
                sexs: [{'value':'男', label:'男'},{'value':'女', label:'女'}],
                sex_change:'',
                nickname_change:'',
                birthday_change:'',
                textarea:'',
                user:{}
            }
        },

        methods:{
            update(){
                if(this.flag=='sex'){
                    this.user['sex'] = this.sex_change
                }
                if(this.flag=='nickname'){
                    this.user['nickname']=this.nickname_change
                }
                if(this.flag=='desc'){
                    this.user['desc'] = this.textarea
                }
                if(this.flag=='birthday'){
                    this.user['birthday'] = this.birthday_change
                }
                Post('/api/user/'+ this.user._id+"/update", this.user).then(data =>{
                    this.$router.push('/mymodify')
                    this.$message({
                        'message':'修改成功！',
                        'type':'success'
                    })
                })
            },




        },

        mounted(){
            getUserInfo().then(data=>{
                this.user=data.data
                console.log(this.flag)
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
