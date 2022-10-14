<template>
  <view class="rule">
    <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
     <img src="https://s1.ax1x.com/2022/10/13/xdhbJ1.png" class="bg" style="width: 750rpx;height: 608rpx;z-index: 2;margin-top:1015rpx;opacity:0.41 ;"></img>
     <img class="return" src="https://s1.ax1x.com/2022/10/13/xdhRzV.png" @click='goHome()'></img>    <img class="title" src="https://s1.ax1x.com/2022/10/13/xdhqRx.png" ></img>
     <view class="rule_1">
       <!-- 标签页 -->
       <scroll-view scroll-x class="bg-white nav tab" scroll-with-animation :scroll-left="scrollLeft">
         <view class="flex text-center">
       			<view class="cu-item flex-sub text-orange text-xxl text" :class="index==TabCur?'text_active text-xxl text-orange cur':''" v-for="(item,index) in tablist" :key="index" @tap="tabSelect" :data-id="index">
       				{{item}}
       			</view>
            </view>
       		</scroll-view>
          <view v-if="0==TabCur" class="play">
            <uni-swiper-dot class="uni-swiper-dot-box" @clickItem=clickItem  :info="info" :current="current"  :mode="mode" :dots-styles="dotsStyles" field="content">
            	<swiper class="swiper-box" @change="change" :current="swiperDotIndex">
            		<swiper-item >
            			<view class="content_1">
            			  <text class="text_1">游戏有三种模式：    </text>          
            			  <text class="text_1">1、本地对战：即两名玩家使用同一设备对战，可离线进行</text>
            			 <text class="text_1">2、人机对战：即应用程序能够实现自动掷骰、决策，与真人玩家进行对战  </text> 
            			  <text class="text_1">3、在线对战：即玩家能够和其他客户端匹配对战</text>
            			</view>
            		</swiper-item>
                <swiper-item  >
                	<view class="content_1">
                	  <text class="text_1">各方初始盘面</text>          
                	 <img src="https://s1.ax1x.com/2022/10/13/xdhgGq.png" alt="" class="tu_1">
                	</view>   
                </swiper-item>
                <swiper-item >
                	<view class="content_1">
                	  <text class="text_1">轮流掷骰：选择己方九宫格的一格放菜骰子</text>          
                	 <img src="https://s1.ax1x.com/2022/10/13/xdhrZQ.png" alt="" class="tu_2">
                	</view>   
                </swiper-item>
                <swiper-item >
                	<view class="content_1">
                	<text class="text_1">开心抢食：己方某线置骰后，对方该线同点数消除</text>          
                	 <img src="https://s1.ax1x.com/2022/10/13/xdh0sS.png" alt="" class="tu_2">
                	 	</view>   
                </swiper-item>
                <swiper-item >
                	<view class="content_1">
                	<text class="text_1">结算规则：当某方九宫格满时，进入结算.玩家得分=(各点数*点数在该列出现次数的平方)之和.各玩家得分=每列得分之和
</text>          
                	 <img src="https://s1.ax1x.com/2022/10/13/xdhcin.png" alt="" class="tu_3">
                	 	</view>   
                </swiper-item>
            	</swiper>
            </uni-swiper-dot>
            </view>
          			
          	
          <view v-if="1==TabCur" class="play">
          			<img class="play_2" src="https://s1.ax1x.com/2022/10/13/xdhyIs.png" ></img>
          		</view>
     </view>
  </view>
</template>

<script>
  export default {
    components: {},
  	data() {
  		return {
  			title: 'rule',
        TabCur: 0,
        scrollLeft: 0,
        tablist:['规则玩法','操作提示'],
        modeIndex: -1,
        styleIndex: -1,
        current: 0,
        mode: 'indexes',
        dotsStyles: {
          backgroundColor: '#fca800',
          border: '1px #fca800 solid',
          color: '#fff',
          selectedBackgroundColor: '#ff7c25',
          selectedBorder: '1px #ff7c25 solid'
        },
        swiperDotIndex: 0,
        info: [{},{},{},{},{}],
  		}
  	},

  	onLoad() {
       
  	},
  	methods: {
      tabSelect(e) {
      				this.TabCur = e.currentTarget.dataset.id;
      				this.scrollLeft = (e.currentTarget.dataset.id - 1) * 60
      			},
       goHome(){
          uni.navigateTo({
             url: '/pages/home/home'   ,   	 　　
         });
       },
       change(e) {
       	this.current = e.detail.current
       },
       selectStyle(index) {
       	this.dotsStyles = this.dotStyle[index]
       	this.styleIndex = index
       },
       selectMode(mode, index) {
       	this.mode = mode
       	this.modeIndex = index
       	this.styleIndex = -1
       	this.dotsStyles = this.dotStyle[0]
       },
       clickItem(e) {
       	this.swiperDotIndex = e
       },
       onBanner(index) {
       	console.log(22222, index);
       }
  	}
  }
</script>

<style>
  page {
      background-color: #f6f6f6;
      height: 100%; 
    }
  .rule{
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
    width: 430rpx;
    height: 250rpx;
    margin-left: 200rpx;
    margin-top: 190rpx;
  }
  .rule_1{
    position: absolute;
    z-index: 2;
    margin-left: 40rpx;
    margin-top: 300rpx;
    width: 670rpx;
    height: 1100rpx;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.7);
    
    border: 2rpx solid #BBBBBB;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction:column;
  }
  .tab{
    background: rgba(255, 255, 255, 0.1);
    margin: 20rpx;
    margin-top: 90rpx;
    width: 630rpx;
  }
  .text{
    font-weight: 600;
    font-size: 50rpx;
  }
  .text_active{
    font-weight: 800;
  }
  .play{
    width: 620rpx;
    height: 870rpx;
    border-radius: 30px;
    margin-left: 25rpx;
   background: rgba(252, 202, 0, 0.5);
    
    
    border: 6rpx solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
  .play_2{
    width: 550rpx;
    height: 570rpx;
    margin-left: 29rpx;
    margin-top: 140rpx;
    border-radius: 30px; 
  }
.swiper-box{
  width: 620rpx;
  height: 870rpx;
  padding: 40rpx;
}
.content_1{
    display: flex;
    flex-direction: column;
}
.text_1{
  font-size: 42rpx;
  font-weight: 600;
  letter-spacing: 20rpx;
  color: #7B4716;
  margin-top: 10rpx;
}
.tu_1{
  width: 560rpx;
  height: 570rpx;
  margin-top: 60rpx;
  border-radius: 30px; 
}
.tu_2{
  width: 560rpx;
  height: 570rpx;
  margin-top: 10rpx;
  border-radius: 30px; 
}
.tu_3{
  width: 560rpx;
  height: 350rpx;
  margin-top: 10rpx;
  border-radius: 30px; 
}
</style>