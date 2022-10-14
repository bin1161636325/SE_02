<template>
	<view class="content">
      <img src="https://s1.ax1x.com/2022/10/13/xdhhsU.jpg" class="bg" style="width: 100%;height: 100%;"></img>
      <view class="play_button">
        <img src="https://s1.ax1x.com/2022/10/13/xd64N6.png" class="play" style="width: 482rpx;height: 248rpx;"  open-type="getUserInfo" @tap="getUserProfile()" ></img>
      </view>
	</view>
</template>
 
<script> 
	export default { 
		data() {
			return {
				title: 'welcome',
        user_url:'',
        user_name:'',
			}
		},
		onLoad() {
       this.$music.playBgm({mute:false})
       console.log(this.$store.state.point_1)
		},
		methods: {
      getUserProfile(e) {
      				// 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
      				// 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
      				wx.getUserProfile({
      					desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      					success: (res) => {
      						console.log(res);
      						this.user_url=res.userInfo.avatarUrl;//获取用户微信头像
      						this.user_name=res.userInfo.nickName;//获取用户微信名
                  this.$store.commit("getUser_url",this.user_url)
                  this.$store.commit("getUser_name",this.user_name)
                  uni.navigateTo({
                      url: '/pages/home/home'   ,   	 　　
                  });
      					}
      				})
      			},
       goHome(){
          
       },
		}
	}
</script>

<style> 
  page {
    background-color: #f6f6f6;
    height: 100%;
    //padding-bottom: constant(safe-area-inset-bottom);
    //padding-bottom: env(safe-area-inset-bottom);
  }
.content{
  width: 100%; 
  height: 100%;
}
.bg{
  position: absolute;
  z-index: 1;
}
.play_button{
  display: flex;
  flex-direction:row;
  justify-content: center;
  width: 100%;
  height: 100%;
}
.play{
  position: absolute;
  margin-top:150%;
  opacity: 0.9;
  z-index: 2;
}
</style>
