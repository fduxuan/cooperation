<template>

    <div id = "Footer" class="footer">
      <el-row>
        <el-col :span="8">
          <router-link to="/task">
            <el-button style="background-color: #D9F9FF"  circle> 任务</el-button>
          </router-link>
        </el-col>
        <el-col :span="8">
          <router-link to="/square">
            <el-button style="background-color: #D9F9FF"  circle> 广场</el-button>
          </router-link>
        </el-col>

        <el-col :span="8">
          <router-link to="/myindex">
            <el-button style="background-color: #D9F9FF"  circle >我的</el-button>
          </router-link>
        </el-col>

      </el-row>
    </div>


</template>

<script>

    export default {
        name: "Footer",
        data() {
            return {

            }
        },
        methods:{
        }
    }



</script>

<style>
  .footer{
    position: fixed;
    bottom:0;
    z-index: 9999;
    width: 100%;
    background-color: #D8EBFD;

  }
</style>
