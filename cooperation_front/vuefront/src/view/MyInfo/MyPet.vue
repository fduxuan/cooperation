<template>
  <el-container>
    <el-header style="height:150px">
      <el-row>
        <h1 style="margin-top: 0px">我的宠物</h1>
      </el-row>
      <el-row>
        当前等级: {{user.pet}}
      </el-row>
      <el-row>
        所有积分: {{user.score}}
      </el-row>
      <el-row>
        下一级所需积分: {{petscore[user.pet]}}
      </el-row>

      <el-row style="align-items: center; text-align: center; color: #795da3" @click="upgrade">
        <i class="el-icon-ice-cream-round" style="font-size: 30px" @click="upgrade"></i>点击升级
      </el-row>
    </el-header>
    <el-main>


      <div id="container">

      </div>


    </el-main>


    <Footer></Footer>
  </el-container>

</template>

<script>
    import Footer from "../../components/Footer";
    import inflate from "../../assets/js/inflate.min";
    import dog from "../../assets/dog.jpg"
    import mouse from "../../assets/mouse.png"
    import hh from "../../assets/house.jpg"

    THREE.inflate = inflate;
    THREE.inflate();
    import FBXLoader from "../../assets/js/FBXLoader";

    import {Post} from "../../model/helper";
    import {getUserInfo} from "../../model/user";
    import crab from "../../assets/crab.fbx";
    import pusheen from "../../assets/pusheen.fbx"
    THREE.FBXLoader = FBXLoader;
    import GLTFLoader from 'three/examples/js/loaders/GLTFLoader';
    THREE.GLTFLoader=GLTFLoader
    import scene from '../../assets/scene.gltf'
    import cat from '../../assets/cat.jpg'
    import house from "../../assets/house.jpeg"

    export default{
        components:{
            Footer,
        },
        data(){
            return {
                camera: null,
                scene: null,
                renderer: null,
                mesh: null,
                // FBXLoader: FBXLoader,
                // inflate: inflate,


                tu:[cat, dog, mouse, hh, cat, cat,cat,cat,cat,cat,cat],
                cat: cat,
                dog: dog,
                flag: cat,
                house: house,
                petscore:['10', '30', '50', '90', '200', '400', '800', '1200'],
                user:{}
            }
        },
        methods: {

            jiazai() {
                // console.log(this);
                // console.log(this.THREE);
                // console.log(THREE);

                let container = document.getElementById('container')
                this.camera = new THREE.PerspectiveCamera(70, container.clientWidth / container.clientHeight, 0.01, 10)
                this.camera.position.z = 0.6
                this.scene = new THREE.Scene()

                let loader = new THREE.FBXLoader();

                let that = this
                let pusheen = this.pusheen
                var materials = [];

                for (var i = 0; i < 6; ++i) {
                    materials.push(new THREE.MeshBasicMaterial({

                        map: THREE.ImageUtils.loadTexture(this.flag,
                            {}, function() {
                                renderer.render(scene, camera);
                            }),
                        overdraw: true
                    }));
                }




                let geometry = new THREE.BoxGeometry(0.2, 0.2, 0.2)
                let material = new THREE.MeshNormalMaterial()
                this.mesh = new THREE.Mesh(geometry, materials)
                this.scene.add(this.mesh)
                this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
                this.renderer.setSize(container.clientWidth, container.clientHeight)
                container.appendChild(this.renderer.domElement)
            },
            animate: function () {
                requestAnimationFrame(this.animate)
                this.mesh.rotation.x += 0.01
                this.mesh.rotation.y += 0.02
                this.renderer.render(this.scene, this.camera)
            },

            async before(){
                let user = await getUserInfo()
                if(user.code !=0){
                    alert("宁没有登录")
                    this.$router.push({path:'/'})

                }
                else{
                    if(user.data['score'] == undefined){
                        user.data['score'] = 10000
                    }
                    if(user.data['pet'] == undefined){
                        user.data['pet'] = 0
                    }
                    this.flag=this.tu[user.data['pet']]
                    console.log(this.flag)
                    this.user = user.data
                }


            },

            async upgrade(){
                if(this.user['score']>=this.petscore[this.user['pet']]){
                    this.user['score'] = this.user['score'] - this.petscore[this.user['pet']]
                    this.user['pet'] = this.user['pet']+1
                    await Post('/api/user/' + this.user._id+ '/update', this.user)


                    this.$message({
                        'message': "升级成功！",
                        'type': "success"
                    })

                }
                else{
                    this.$message({
                        'message': "宁的积分还不够！",
                        'type': "warning"
                    })
                }

            }
        },
        mounted () {
            this.before().then(res=>{
                this.jiazai()
            })

            this.animate()
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
  .message{
    margin-top: 10px;
    margin-right: 40px;
  }
  .small-box{
    background-color: #B8CDE6;
    margin: 10px;
    height: 50px;
    display: flex;
    align-items: center;
  }
  #container{
    height:400px;
    background: url("../../assets/house.jpeg") ;
  }

</style>
