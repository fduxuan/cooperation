<template>
  <el-container>
    <el-header>
      <h1>{{findData}}</h1>
    </el-header>
    <el-main>

    </el-main>

    <el-footer>
      <p style="color: grey">了解更多</p>
    </el-footer>
  </el-container>

</template>



<script>
    import axios from "axios";
    import qs from 'querystring'
    import {Post} from '../model/helper.js'
    export default{
        data(){
            return {
                findData:""
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

        },

        mounted(){
            this.userFind()
        }
    }

</script>
