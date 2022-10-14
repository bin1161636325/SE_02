<template>
  <view class="over">
    <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
     <img src="https://s1.ax1x.com/2022/10/13/xdhbJ1.png" class="bg" style="width: 750rpx;height: 608rpx;z-index: 2;margin-top:1015rpx;opacity:0.41"></img>
     <img src="https://s1.ax1x.com/2022/10/13/xdhLz6.png" class="over_zi" ></img>
     <img src="https://s1.ax1x.com/2022/10/13/xd62u9.png" class="king" ></img>
     
     <view class="over_1">
       <view class="play_1">
         <view class="people">
           <img :src="play1_url" alt="" style="width:120rpx;height:120rpx">
         </view>
         <view class="point">
           {{point_1}}
         </view>
       </view>
       <view class="play_2">
         <view class="people">
           <img :src="play2_url" alt="" style="width:120rpx;height:120rpx">
         </view>
         <view class="point">
           {{point_2}}
         </view>
       </view>
     </view>
     <view class="button">
         <img class="return" src="https://s1.ax1x.com/2022/10/13/xdhRzV.png" @click='goRobot()'></img>      
         <img class="home" src="https://s1.ax1x.com/2022/10/14/xdjdtf.png" @click='goHome()' ></img>   
         <img class="rank" src="https://s1.ax1x.com/2022/10/13/xdh4LF.png" @click='goRank()' ></img>
     </view>
     
  </view>
</template>

<script> 
  export default {
  	data() {
  		return {
  			title: 'gameOver',
        user_name:"欣欣",
        user_picture_url:"",
        user_point:"520",
        user_phone:"520",
        winner:'',
        point_1:0,
        loser:'',
        point_2:0,
        play1_url:'',
        play2_url:'',
        play1_name:'',
        play2_name:'',
  		}
  	},
  	onLoad() {
      this.winner=this.$store.state.winner
      this.loser=this.$store.state.loser
      this.point_1=this.$store.state.point_1
      this.point_2=this.$store.state.point_2
      this.play1_url=this.$store.state.play1_url
      this.play2_url=this.$store.state.play2_url
      this.play1_name=this.$store.state.play1_name
      this.play2_name=this.$store.state.play2_name
      console.log(this.play1_name)
      console.log(this.play2_name)
      this.addrank1()
      this.addrank2()
  	},
  	methods: {
       goHome(){
          uni.navigateTo({
             url: '/pages/home/home'   ,   	 　　
         });
       },
       goRobot()
       {
            uni.navigateTo({
               url: '/subpkg/robotGame/robotGame'
               })
        },
       goRank(){
          uni.navigateTo({
             url: '/subpkg/rank/rank'
             })
        },
        addrank1(){
          console.log(this.play1_name, this.user_phone, this.play1_url, this.point_1);
          let that = this;
          wx.request({
            url: 'http://192.168.43.236:8000/api/addrank/',
            data: {player_name: this.play1_name, player_picture_url: this.play1_url, player_phone: this.user_phone, player_point: this.point_1},
            method: 'POST',
          success: function(res) {
            console.log(res);
          }
          })
          },
          addrank2(){
            console.log(this.play2_name, this.user_phone, this.play2_url, this.point_2);
            let that = this;
            wx.request({
              url: 'http://192.168.43.236:8000/api/addrank/',
              data: {player_name: this.play2_name, player_picture_url: this.play2_url, player_phone: this.user_phone, player_point: this.point_2},
              method: 'POST',
            success: function(res) {
              console.log(res);
            }
            })
            },
  	}
  }
</script>

<style>
  page {
      background-color: #f6f6f6;
      height: 100%; 
    }
  .over{
    width: 100%; 
    height: 100%;
  }
  .bg{
    position: absolute;
    z-index: 1;
  }
  .over_1{
    position: absolute;
    z-index: 2;
    margin-left: 60rpx;
    margin-top: 300rpx;
    width: 620rpx;
    height: 770rpx;
   
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.7);
    
    border: 2rpx solid #BBBBBB;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction:column;
  }
  .play_1{
    display: flex;
    flex-direction:row;
    width: 520rpx;
    height: 220rpx;
    margin-left: 40rpx;
    margin-top: 120rpx;
    opacity: 1;
    border-radius: 30px;
    background: #FCCA00;
    
    border: 10rpx solid #FFFFFF;            
    
    box-shadow: 0px 2px 6px 1px #E99D42;
  }
  .play_2{
    display: flex;
    flex-direction:row;
    width: 520rpx;
    height: 220rpx;
    margin-left: 40rpx;
    margin-top: 80rpx;
    opacity: 1;
    border-radius: 30px;
    background: #FCCA00;
    
    border: 10rpx solid #FFFFFF;            
    
    box-shadow: 0px 2px 6px 1px #E99D42;
  }
  .people{
    margin-left: 45rpx;
    margin-top: 50rpx;
    width: 120rpx;
    height: 120rpx;
    opacity: 1;
    border-radius: 10px;
    background: rgba(255, 255, 255, 1);
    
    border: 6rpx solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px #FFBF6B;
    
  }
  .point{
    font-size: 100rpx;
    font-weight: 600;
    letter-spacing: 0px;
    color: #7B4716;
    text-align: center;
    line-height: 220rpx;
    margin-left: 90rpx;
  }
  .over_zi{
    position: absolute;
    width: 400rpx;
    height: 200rpx;
    z-index: 3;
    margin-top:200rpx;
    transform: rotate(355deg);
    margin-left: 200rpx;
  }
  .king{
    position: absolute;
    margin-top:310rpx;
    transform: rotate(342deg);
    margin-left: 60rpx;
    width: 140rpx;
    height: 140rpx;
    z-index: 3;
  }
  .button{
    position: absolute;
    display: flex;
    flex-direction:row;
    opacity: 0.8;
    z-index: 2;
    margin-left: 60rpx;
    margin-top: 1110rpx;
    width: 620rpx;
    height: 300rpx;
  }
  .return{
    width: 150rpx;
    height: 150rpx;
    margin-top: 40rpx;
    border-radius: 15px;
    background: #FEFA83;
    
    border: 10rpx solid #FFFFFF;            
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
  .home{
    width: 190rpx;
    height: 190rpx;
    margin-left: 50rpx;
    border-radius: 15px;
    background: #FEFA83;
    
    border: 10rpx solid #FFFFFF;            
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
  .rank{
    width: 150rpx;
    height: 150rpx;
    margin-left: 50rpx;
     margin-top: 40rpx;
     border-radius: 15px;
     background: #FEFA83;
     
     border: 10rpx solid #FFFFFF;            
     box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
</style>