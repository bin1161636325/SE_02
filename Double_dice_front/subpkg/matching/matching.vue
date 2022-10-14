<template>

<view class="matching">
     <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
      <img src="https://s1.ax1x.com/2022/10/13/xdhbJ1.png" class="bg" style="width: 750rpx;height: 608rpx;z-index: 2;margin-top:1015rpx;opacity:0.41 ;"></img>
      <img class="return" src="https://s1.ax1x.com/2022/10/13/xdhRzV.png" @click='goHome()'></img>     <img class="title" src="https://c2.im5i.com/2022/10/11/TGBww.png" ></img>
      <view class="matching_1">
        <view class="play">
          
        </view>
        <view class="play">
          <view class="people" >
              <img :src="user_url" alt="" style="width: 160rpx;
          height: 160rpx;">
            </view>
            <view class="name">
               {{user_name}}
            </view>
        </view>
      </view>
      <view class="button" @click="goOnline()">
        {{start}}
      </view>
</view>
</template>

<script>
  var socket = null;
  export default {
  	data() {
  		return {
  			title: 'matching',
        start:'开始匹配',
        start_num:0,
        other_name:'',
        other_url:'',
        user_url:'',
        user_name:'',
        play1_name:'', 
        play2_name:'',  
        play1_url:'',  
        play2_url:'',  
        first:0,
  		}
  	},
  
  	onLoad() {
     this.user_name=this.$store.state.user_name
     this.user_url=this.$store.state.user_url 
     var that = this;
     // 创建websocket
     // 正式地址使用wss
     socket = wx.connectSocket({
         url: 'ws://192.168.43.236:8000/room/' + 'ready' + '/',
         success: function(res) {
             console.info('创建连接成功');
             //socketTaskId: 22
             // console.info(res);
         }
     });
     // 事件监听
     socket.onOpen(function () {
         console.info('连接打开成功');
     });
     socket.onClose(function () {
         console.info('连接关闭成功');
     });
     socket.onError(function () {
         console.info('连接报错');
     });
     socket.onMessage(function(res){
       console.log(res);
       var data = res.data;
       console.log(data)
       var json = JSON.parse(data);
       if (json.start != undefined){
         that.other_name = json.other_name
         that.other_url = json.other_url
         that.play1_name = json.play1_name
         that.play2_name = json.play2_name
         that.play1_url = json.play1_url
         that.play2_url = json.play2_url
         that.$store.commit("getFirst",json.first)
         that.$store.commit("getOther_name",that.other_name)
         that.$store.commit("getOther_url",that.other_url)
         that.$store.commit("getPlay1_url",that.play1_url)
         that.$store.commit("getPlay2_url",that.play2_url)
         that.$store.commit("getPlay1_name",that.play1_name)
         that.$store.commit("getPlay2_name",that.play2_name)
         that.start_num = json.start;
         if (that.start_num == 1){
          that.start='匹配成功'
          socket.close();
           uni.navigateTo({
               url: '/subpkg/onlineGame/onlineGame'   ,  
          }) 
         }
       }
     })
  	},
  	methods: {
       goHome(){
         socket.close();
          uni.navigateTo({
             url: '/pages/home/home'   ,   	 　　
         });
         },
          goOnline()
       {
         let that=this
         that.start='正在匹配中...'
         socket.send({
           data:JSON.stringify({user_url: this.user_url, user_name: this.user_name}),
           success:function(res){
             console.log('正在匹配成功');
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
  .matching{
    width: 100%; 
    height: 100%;
  }
  .bg{
    position: absolute;
    z-index: 1;
  }
  .return{
    position: absolute;
    z-index: 2;
    width: 160rpx;
    height: 160rpx;
    margin-left: 60rpx;
    margin-top: 130rpx;
  }
  .title{
    position: absolute;
    z-index: 3;
    width: 680rpx;
    height: 310rpx;
    margin-left: 60rpx;
    margin-top: 290rpx;
    transform: rotate(355deg);
  }
  .matching_1{
    position: absolute;
    z-index: 2;
    margin-left: 40rpx;
    margin-top: 400rpx;
    width: 670rpx;
    height: 750rpx;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.7);
    
    border: 2rpx solid #BBBBBB;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction:column;
  }
  .play{
    display: flex;
    flex-direction: row;
    width: 580rpx;
    height: 240rpx;
    border-radius: 30px;
    margin-left: 43rpx;
    margin-top: 100rpx;
    background: rgba(252, 202, 0, 0.5);
    
    border: 6rpx solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
  .button{
    position: absolute;
    z-index: 2;
    width: 400rpx;
    height: 160rpx;
    margin-top: 1200rpx;
    margin-left: 150rpx;
    background-color: #A16222;
    border: 10rpx solid #ffffff; 
    border-radius: 30px;
    font-size: 23px;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 150rpx;
    color: rgba(255, 255, 255, 1);
    text-align: center;
  }
  .people{
    margin-left: 45rpx;
    margin-top: 25rpx;
    width: 160rpx;
    height: 160rpx;
    opacity: 1;
    border-radius: 10px;
    background: rgba(255, 255, 255, 1);
    
    border: 3px solid rgba(255, 195, 0, 1);            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  
  }
  .name{
    margin-top: 72rpx;
    width: 220rpx;
    height: 80rpx;
    opacity: 1;
    border-radius: 8px;
    background: rgba(233, 157, 66, 1);
    
    border: 3px solid rgba(252, 202, 0, 1);            
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 80rpx;
    color: rgba(255, 255, 255, 1);
    text-align: center;
    
  }
</style>