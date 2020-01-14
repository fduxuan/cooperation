<template>
  <el-container>
    <el-header>
      <el-row>
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane  v-for="item in tags" :key="item"  :label="item" :name="item"></el-tab-pane>
            <el-tab-pane label="更多" name="更多"></el-tab-pane>
          </el-tabs>
      </el-row>

      <el-row class="small-box-2">
        <el-col :span="18">
          <el-input size="small" v-model="search" placeholder="请输入搜索内容"></el-input>
        </el-col>
        <el-col :span="2" :offset="2">
          <i style="font-size:20px" class="el-icon-search" @click="searchDetail"></i>
        </el-col>
      </el-row>

    </el-header>
    <br>
    <br>
    <el-main>
      <el-row>
        <el-carousel height="180px">
          <el-carousel-item v-for="item in advertisements" :key="item">
            <el-image :src="item"></el-image>
          </el-carousel-item>
        </el-carousel>
      </el-row>
      <div>
        <h1>{{activeName}}计划</h1>
      </div>
      <div class="big-box" v-if="plans.length > 0">

        <el-row v-for="item in plans" :key="item._id" style="margin-top: 5px;">
          <router-link class="route-link" :to="{ name: 'plandetail', params: { pid: item._id } }">
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

        <el-row>暂无数据</el-row>
      </div>
      <br>
    </el-main>

    <Footer></Footer>
  </el-container>

</template>

<script>
  import Footer from "../components/Footer";
  import qs from 'querystring'
  import {Post} from '../model/helper.js'
  import ad_1 from "@/assets/ad_1.jpg"
  import ad_2 from "@/assets/ad_2.jpg"
  import ad_3 from "@/assets/ad_3.jpg"
  import test_1 from "@/assets/test_1.jpg"

  export default{
      components:{
          Footer,
      },
      data(){
          return {
              findData:"",
              test_1: test_1,
              tags:['推荐','学习','饮食','运动','英语'],
              activeName: '推荐',
              search:"",
              advertisements:[ad_1, ad_2, ad_3],
              plans:[]
          }
      },

      methods:{
          userFind() {
              let query = {}
              Post('/api/user/find',qs.stringify(query), {
              }).then(response => {
                  this.findData = response.data
              })
          },

          handleClick(tab) {
              console.log(tab.name);
              this.search=""
              let query = undefined
              if(tab.name=='推荐') {
                  query = {}
              }
              else if (tab.name == "更多"){
                  query = {"tag": {"$nin": ['学习','饮食','运动','英语']}}
              }
              else {
                  query = {'tag': tab.name}
              }
              this.getPlans(query)

          },


          getPlans(query=undefined){
              Post('/api/plan/find', {filter: query}).then(data=>{
                  console.log(data.data)
                  this.plans=data.data
              })
          },

          searchDetail(){
              let data = this.search
              if(data == ""){
                  this.$message({
                      'message': '输入不可为空！',
                      'type': "warning"
                  })
              }
              let query = {"$or": [{"desc":{"$regex": data}}, {"tag": data}]}
              this.activeName="搜索"
              this.getPlans(query)

          }
      },

      mounted(){
          this.userFind()
          this.getPlans()
      }
  }

</script>

<style>
 .footer{
   position: fixed;
   bottom:0;
   z-index: 9999;
   width: 100%;
   background-color: #E6EEFF;
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
