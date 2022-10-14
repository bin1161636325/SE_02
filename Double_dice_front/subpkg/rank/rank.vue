<template>
  <view class="rank">
    <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
     <img src="https://s1.ax1x.com/2022/10/13/xdhbJ1.png" class="bg" style="width: 750rpx;height: 608rpx;z-index: 2;margin-top:1015rpx;opacity:0.41 ;"></img>
     <img class="return" src="https://s1.ax1x.com/2022/10/13/xdhRzV.png" @click='goHome()'></img>    <img class="title" src="https://s1.ax1x.com/2022/10/13/xdhHiR.png" ></img>
     <view class="rank_1">
       <!-- 标签页 -->
       <scroll-view scroll-x class="bg-white nav tab" scroll-with-animation :scroll-left="scrollLeft">
         <view class="flex text-center">
       			<view class="cu-item flex-sub text-orange text-xxl text" :class="index==TabCur?'text_active text-xxl text-orange cur':''" v-for="(item,index) in tablist" :key="index" @tap="tabSelect" :data-id="index">
       				{{item}}
       			</view>
            </view>
       		</scroll-view>
          <view v-if="0==TabCur">
            <scroll-view v-if="refresh==1" class="total" scroll-y="true">
              <view class="" v-for="(item,index) in ranklist" :key="index">
                <view class="item">
                  
                  <view class="num">
                     {{index+1}}
                  </view>
                  <view class="people">
                    <img :src="item.picture_url" alt="" style="width:108rpx;height:108rpx">
                  </view>
                  <view class="point">
                    {{item.point}}
                  </view>
                </view>
                
              </view>
            </scroll-view>
            <view class="my">
              <view class="num_1">
                 {{my_rank}}
              </view>
              <view class="people">
                <img :src="user_url" alt="" style="width:108rpx;height:108rpx">
              </view>
              <view class="point">
                {{my_point}}
              </view>
            </view>
            </view>
          <view v-if="1==TabCur" class="play">
          			
          		</view>
          <view v-if="2==TabCur" class="play">
              			
          </view>
     </view>
  </view>
</template>

<script>
  export default {
    components: {},
  	data() {
  		return {
  			title: 'rank',
        TabCur: 0,
        scrollLeft: 0,
        tablist:['总榜','个人榜','好友榜'],
        ranklist:[],
        my_point:0,
        my_rank:0,
        user_phone:"1846612541",
        refresh:0,
        user_url:'',
        user_name:'',
  		}
  	},

  	onLoad() {
      this.user_url=this.$store.state.user_url
      this.user_name=this.$store.state.user_name
      this.Rankinglist()
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
       Rankinglist(){
         let that=this
         wx.request({
           url:'http://192.168.43.236:8000/api/rankinglist/',
           data:{player_name: this.user_name, player_picture_url: this.user_url, player_phone: this.user_phone},
           method:'POST',
           success: function(res){
             console.log(res.data)
             let i=0;
             for(;i<res.data.length-1;i++){
               // console.log(res.data[i]);
               that.ranklist[i]=res.data[i]
               
               // console.log(that.ranklist)
             }
             // console.log(res.data[i].point) // res.data[i].rank
             that.my_point=res.data[i].point
             that.my_rank=res.data[i].rank
             that.refresh=1
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
  .rank{
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
    width: 520rpx;
    height: 220rpx;
    margin-left: 170rpx;
    margin-top: 200rpx;
    transform: rotate(355deg);
  }
  .rank_1{
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
  .total{
    width: 580rpx;
    height: 690rpx;
    border-radius: 30px;
    margin-left: 43rpx;
    margin-top: 20rpx;
    background: rgba(252, 202, 0, 0.5);
    
    border: 6rpx solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
  }
  .item{
    width: 540rpx;
    height: 135rpx;
    border-bottom: #FFBF6B solid 6rpx;
    display: flex;
    flex-direction: row;
  }
  .my{
    width: 648rpx;
    height: 138rpx;
    border-radius: 20px;
    margin-left: 9rpx;
    margin-top: 40rpx;
    background: rgba(252, 202, 0, 0.5);
    
    border: 6rpx solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: row;
  }
  
  .people{
    margin-top: 5rpx;
    margin-left: 70rpx;
    width: 120rpx;
    height: 120rpx;
    opacity: 1;
    border-radius: 10px;
    background: rgba(255, 255, 255, 1);
    
    border: 3px solid #E99D42;            
    
    box-shadow: 0px 2px 6px 1px #FFBF6B;
    
  }
  .point{
    margin-top: 20rpx;
    width: 220rpx;
    height: 80rpx;
    opacity: 1;
    border-radius: 10px;
    background: #FFBF6B;
    
    border: 3px solid #E99D42;            
    /** 文本1 */
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: rgba(255, 255, 255, 1);
    text-align: center;
    line-height: 80rpx;
  }
  .num{
    margin-left: 20rpx;
    width: 90rpx;
    height: 135rpx;
    opacity: 1;      
    /** 文本1 */
    font-size: 60rpx;
    font-weight: 550;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
    text-align: center;
    line-height: 135rpx;
    }
  .num_1{
    margin-left: 60rpx;
    width: 90rpx;
    height: 135rpx;
    opacity: 1;      
    /** 文本1 */
    font-size: 60rpx;
    font-weight: 550;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
    text-align: center;
    line-height: 135rpx;
  }
</style>