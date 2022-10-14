<template>
  <view class="home">
    <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
    <img src="https://s1.ax1x.com/2022/10/13/xdhbJ1.png" class="bg" style="width: 750rpx;height: 608rpx;z-index: 2;margin-top:1015rpx;"></img>
     <view class="home_1">
    <view class="song" >
      <img src="https://s1.ax1x.com/2022/10/13/xdhTo9.png" v-if="no==0" @click="stop()" style="width: 55px; height: 55px;opacity: 1;"> 
      <img src="https://s1.ax1x.com/2022/10/13/xdhfMT.png" v-if="no==1" @click="stop()" style="width: 55px; height: 55px;opacity: 1;"> 
      <img src="https://s1.ax1x.com/2022/10/13/xdhodJ.png"style="width: 35px; height: 35px;opacity: 1;">
    </view>
    <view class="people_rule">
      <view class="people" > 
        <img :src="user_url" alt="" style="width: 180rpx;
    height: 180rpx;">
      </view>
      <view class="name">
         {{user_name}}
      </view>
      <view class="rule" @click="goRule()">
        <view class="rule_zi">
          规则
        </view>
        <img src="https://s1.ax1x.com/2022/10/13/xdh2R0.png"style="width: 90px;height: 90px;opacity: 1;">
      </view>
    </view>
    <view class="mode_1">
      <view class="rank_local">
        <view class="rank">
           <img src="https://s1.ax1x.com/2022/10/13/xd6T3D.png"  style="width: 320rpx;height: 180rpx;opacity: 1;box-shadow: 0px 2px 6px 3px rgba(0, 0, 0, 0.25);border-radius: 10px;" @click="goRank()">
           <img src="https://s1.ax1x.com/2022/10/13/xd6HjH.png" class="tab" style="width: 320rpx;height: 180rpx;opacity: 1;box-shadow: 0px 2px 6px 3px rgba(0, 0, 0, 0.25);border-radius: 10px;" @click="goMatching()">
        </view>
        <view class="local">
          <img src="https://s1.ax1x.com/2022/10/13/xdhXQK.png" class="lab" style="width: 310rpx;height: 380rpx;opacity: 1;box-shadow: 0px 2px 6px 3px rgba(0, 0, 0, 0.25);border-radius: 10px;" @click="goLocal()">
        </view>
      </view>
    </view>
    <view class="mode_2">
      <view class="friend">
        <img src="https://s1.ax1x.com/2022/10/13/xd6qud.jpg" class="lab" style="width: 250rpx;height: 200rpx;opacity: 1;box-shadow: 0px 2px 6px 3px rgba(0, 0, 0, 0.25);border-radius: 10px;" @click="goFriend()">
      </view>
      <view class="robot">
        <img src="https://s1.ax1x.com/2022/10/13/xd6jEt.png" class="lab" style="width: 400rpx;height: 330rpx;opacity: 1;" @click="goRobot()">
      </view>
    </view>
  </view>
 
  </view>
</template>

<script>
export default {
data() {
			return {
				title: 'home',
        no:0,
        name:0,
        user_url:'',
        user_name:'',
			}
},
destroyed() {
		
		    },
onLoad() {
       // const innerAudioContext = getApp().innerAudioContext;
       console.log(this.$store.state)
       this.user_name=this.$store.state.user_name
       this.user_url=this.$store.state.user_url
       console.log(this.user_url)
       console.log(this.user_name)
		        },
methods:{
       goOver()
       {
         uni.navigateTo({
            url: '/subpkg/gameOver/gameOver'
            })
       },
       goRule()
      {
           uni.navigateTo({
              url: '/subpkg/rule/rule'
              })
       },
       goRank()
       {
            uni.navigateTo({
               url: '/subpkg/rank/rank'
               })
        },
        goMatching()
        {
             uni.navigateTo({
                url: '/subpkg/matching/matching'
                })
         },
         goLocal()
         {
              uni.navigateTo({
                 url: '/subpkg/localGame/localGame'
                 })
          },
          goFriend()
          {
               uni.navigateTo({
                  url: '/subpkg/friend/friend'
                  })
           },
           goRobot()
           {
                uni.navigateTo({
                   url: '/subpkg/robotGame/robotGame'
                   })
            },
            stop(){
              //this.innerAudioContext.pause();
              //this.innerAudioContext.onPause(function() {
                    					//console.log('暂停播放');
                    					//innerAudioContext.startTime = innerAudioContext.currentTime;
                    				 // });
                 this.muteBgMusic = !this.muteBgMusic
                                 console.log(this.muteBgMusic,this.muteBgMusic?'已关闭音乐####':'已开启音乐####');      
                                 if (this.muteBgMusic) {
                                     // 开启静音
                                     this.$music.playBgm({mute:true})
                                     this.no=1
                                 } else {
                                     // 关闭 静音
                                     this.$music.playBgm({mute:false})
                                     this.no=0
                                 }
                          
            }
        
		        }

		}
    
</script>

<style>
  page {
      background-color: #f6f6f6;
      height: 100%; 
    }
  .home{
    width: 100%; 
    height: 100%;
  }
  .bg{
    position: absolute;
    z-index: 1;
  }
  .home_1{
    position: absolute;
    z-index: 2;
  }
  .song{
    margin-left: 45rpx;
    margin-top: 70rpx;
    
  }
  .people_rule{
    display: flex;
    flex-direction:row;
  }
  .people{
    margin-left: 45rpx;
    margin-top: 50rpx;
    width: 180rpx;
    height: 180rpx;
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
  .rule{
    margin-left: 33px;
    margin-top: 80px;
  }
  .rule_zi{
    position: absolute;
    z-index: 3;
    padding-top: 30px;
    padding-left: 23px;
     /** 文本1 */
     font-size: 20px;
     font-weight: 600;
     letter-spacing: 0px;
     line-height: 0px;
     color: rgba(255, 255, 255, 1);
     text-align: center;
     vertical-align: top;

  }
  .rank_local{
    margin-left: 45rpx;
    margin-top: 25rpx;
    display: flex; 
    flex-direction:row;
    width: 369rpx;
  }
  .rank{
    display: flex;
    flex-direction:column;
  }
  .tab{
    margin-top: 20rpx;
  }
  .local{
    margin-left: 35rpx;
  }
  .friend{
    margin-left: 45rpx;
    margin-top: 25rpx;
  }
  .mode_2{
    display: flex;
    flex-direction:row;
  }
  .robot{
    margin-left: 25rpx;
    margin-top: 25rpx;
  }
</style>