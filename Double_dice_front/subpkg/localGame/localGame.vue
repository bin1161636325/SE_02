<template>
  <view class="local">
    <img src="https://s1.ax1x.com/2022/10/13/xd67ge.png" class="bg" style="width: 100%;height: 100%;z-index: 1;"></img>
    <img src="https://s1.ax1x.com/2022/10/13/xd6Uns.png" class="bg" style="width: 450rpx;height: 450rpx;z-index: 1;margin-top: 350rpx;margin-left: 150rpx;"></img>
    <view class="line">
    </view>
    <img src="https://s1.ax1x.com/2022/10/13/xd6Uns.png" class="bg" style="width: 450rpx;height: 450rpx;z-index: 1;margin-top: 950rpx;margin-left: 150rpx;"></img>
    <view class="local_1">
      <view class="p_n"> 
        <view class="people">
          <img :src="robot_url" alt="" style="width:160rpx;height:160rpx">
        </view>
        <view class="name">
           玩家1
        </view>
        <view class="point">
            {{point_1}} 
        </view>
        <view class="place">
        </view>
        <view class="dice_1">
             <img :src="dice_c1" style="width: 120rpx;height: 120rpx;z-index: 3;margin-left: 50rpx;margin-top: 20rpx;"></img>
        </view>
      </view>
      
      <view v-if="dice_c1 === ''" class="touzi_1" @click="touzi_1()">
        <img src="https://s1.ax1x.com/2022/10/13/xd6OHI.png" class="" style="width: 150rpx;height: 120rpx;z-index: 1;margin-top: -30rpx;margin-left: 600rpx;opacity: 1;"></img>
      </view>
      <view v-else class="touzi_1" >
        <img src="https://s1.ax1x.com/2022/10/13/xd6OHI.png" class="" style="width: 150rpx;height: 120rpx;z-index: 1;margin-top: -30rpx;margin-left: 600rpx;opacity: 1;"></img>
      </view>
      
      <view class="column_point_1">
        <view class="column_point">
          {{column_point_11}}
        </view>
        <view class="column_point">
          {{column_point_12}}
        </view>
        <view class="column_point">
          {{column_point_13}}
        </view>
      </view>
    </view>
    <view class="local_2">
      <view class="p_n_2">
        <view class="place_2">
        </view>
       
        <view class="point_2">
          {{point_2}} 
        </view>
        <view class="name_2">
        玩家2
        </view>
        <view class="people_2">
          <img :src="user_url" alt="" style="width:160rpx;height:160rpx">
        </view>
      </view>
   </view>
   
      <view v-if="dice_c2 === ''" class="touzi_2" @click="touzi_2()">
       <img src="https://s1.ax1x.com/2022/10/13/xd6OHI.png" class="" style="width: 150rpx;height: 120rpx;z-index: 1;margin-top: 1320rpx;margin-left: 0rpx;opacity: 1;"></img>
      </view>
      <view v-else class="touzi_2" >
        <img src="https://s1.ax1x.com/2022/10/13/xd6OHI.png" class="" style="width: 150rpx;height: 120rpx;z-index: 1;margin-top: 1320rpx;margin-left: 0rpx;opacity: 1;"></img>
      </view>
      
       <view class="dice_2">
             <img :src="dice_c2" style="width: 120rpx;height: 120rpx;z-index: 3;margin-left: 50rpx;margin-top: 20rpx;"></img>
       </view>
      <view class="column_point_2">
        <view class="column_point">
          {{column_point_21}}
        </view>
        <view class="column_point">
          {{column_point_22}}
        </view>
        <view class="column_point">
          {{column_point_23}}
        </view>
      </view>
   
     <view class="play_1">
     			<view v-if="player1_chess[0] === 0" class="item" @click="clickItem1(0)" >
     				<img src="" style="width: 100%;height: 100%;"></img>
     			</view>
          <view v-else class="item">
          	<img :src="dice_n10" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[1] === 0" class="item" @click="clickItem1(1)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n11" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[2] === 0" class="item" @click="clickItem1(2)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n12" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[3] === 0" class="item" @click="clickItem1(3)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n13" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[4] === 0" class="item" @click="clickItem1(4)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n14" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[5] === 0" class="item" @click="clickItem1(5)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n15" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[6] === 0" class="item" @click="clickItem1(6)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n16" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[7] === 0" class="item" @click="clickItem1(7)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n17" style="width: 100%;height: 100%;"></img>
          </view>
          
          <view v-if="player1_chess[8] === 0" class="item" @click="clickItem1(8)" >
          	<img src="" style="width: 100%;height: 100%;"></img>
          </view>
          <view v-else class="item">
          	<img :src="dice_n18" style="width: 100%;height: 100%;"></img>
          </view>
     		</view>
     <view class="play_2">
    			<view v-if="player2_chess[0] === 0" class="item" @click="clickItem2(0)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n20" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[1] === 0" class="item" @click="clickItem2(1)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n21" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[2] === 0" class="item" @click="clickItem2(2)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n22" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[3] === 0" class="item" @click="clickItem2(3)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n23" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[4] === 0" class="item" @click="clickItem2(4)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n24" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[5] === 0" class="item" @click="clickItem2(5)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n25" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[6] === 0" class="item" @click="clickItem2(6)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n26" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[7] === 0" class="item" @click="clickItem2(7)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n27" style="width: 100%;height: 100%;"></img>
    			</view>
    			
    			<view v-if="player2_chess[8] === 0" class="item" @click="clickItem2(8)" >
    				<img src="" style="width: 100%;height: 100%;"></img>
    			</view>
    			<view v-else class="item">
    				<img :src="dice_n28" style="width: 100%;height: 100%;"></img>
    			</view>
  </view>
  </view>
</template>

<script>
  export default {
  	data() {
  		return {
  			title: 'localGame',
        point_1:0,
        point_2:0,
        dice_1:0,
        dice_2:0,
        dice_c1:'',
        dice_c2:'',
        column_point_11:0,
        column_point_12:0,
        column_point_13:0,
        column_point_21:0,
        column_point_22:0,
        column_point_23:0,
        dice_n10:'',
        dice_n11:'',
        dice_n12:'',
        dice_n13:'',
        dice_n14:'',
        dice_n15:'',
        dice_n16:'',
        dice_n17:'',
        dice_n18:'',
        dice_n20:'',
        dice_n21:'',
        dice_n22:'',
        dice_n23:'',
        dice_n24:'',
        dice_n25:'',
        dice_n26:'',
        dice_n27:'',
        dice_n28:'',
        first:Math.floor(Math.random()*10) % 2,
        player1_chess:[0,0,0,0,0,0,0,0,0],
        player2_chess:[0,0,0,0,0,0,0,0,0],
        player1_index:0,
        player2_index:0,
        gameover:0,
        winner:'',
        loser:'',
        user_name:'',
        user_url:'',
        play1_name:"local",
        play2_name:"",
        robot_url:'https://s1.ax1x.com/2022/10/13/xd3SpT.png',
  		}
  	},
  	onLoad() {
       this.showmodal()
       this.user_name=this.$store.state.user_name
       this.user_url=this.$store.state.user_url
       this.play2_name=this.$store.state.user_name
  	},
  	methods: {
       showmodal(){
         console.log(this.first)
         if(this.first == 0){
           uni.showModal({
               content: '玩家1获得先手',
               showCancel:false,
               confimrText:'开始游戏',
               confirmColor:'#7B4716',
               success: function (res) {
                   if (res.confirm) {
                       console.log('用户点击确定');
                   } else if (res.cancel) {
                       console.log('用户点击取消');
                   }
               }
           });
         }
         else if(this.first == 1){
           uni.showModal({
               content: '玩家2获得先手',
               showCancel:false,
               confimrText:'开始游戏',
               confirmColor:'#7B4716',
               success: function (res) {
                   if (res.confirm) {
                       console.log('用户点击确定');
                   } else if (res.cancel) {
                       console.log('用户点击取消');
                   }
               }
           });
         }
       },
       touzi_1(){
         let that = this
         wx.request({
           url: 'http://192.168.43.236:8000/api/rolldice/',
           data: {},
           method: 'POST',
           success: function(res) {
             console.log(res);
             that.dice_1 = res.data.dice;
             if(that.dice_1==1)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xd6LDA.png'
             }else if(that.dice_1==2)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xdcp8S.png'
             }else if(that.dice_1==3)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xdcSC8.png'
             }else if(that.dice_1==4)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xdc9gg.png'
             }else if(that.dice_1==5)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xd6x4f.png'
             }else if(that.dice_1==6)
             {
               that.dice_c1='https://s1.ax1x.com/2022/10/13/xd6vUP.png'
             }
           }
         })
       },
       touzi_2(){
         let that = this
         wx.request({
           url: 'http://192.168.43.236:8000/api/rolldice/',
           data: {},
           method: 'POST',
           success: function(res) {
             console.log(res);
             that.dice_2 = res.data.dice;
             if(that.dice_2==1)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xd6LDA.png'
             }else if(that.dice_2==2)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xdcp8S.png'
             }else if(that.dice_2==3)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xdcSC8.png'
             }else if(that.dice_2==4)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xdc9gg.png'
             }else if(that.dice_2==5)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xd6x4f.png'
             }else if(that.dice_2==6)
             {
               that.dice_c2='https://s1.ax1x.com/2022/10/13/xd6vUP.png'
             }
           }
         })
       },
       clickItem1(a){
         let that=this
         if(a==0)
         {
           that.dice_n10=that.dice_c1
         }else if(a==1){
           that.dice_n11=that.dice_c1
         }else if(a==2){
           that.dice_n12=that.dice_c1
         }else if(a==3){
           that.dice_n13=that.dice_c1
         }else if(a==4){
           that.dice_n14=that.dice_c1
         }else if(a==5){
           that.dice_n15=that.dice_c1
         }else if(a==6){
           that.dice_n16=that.dice_c1
         }else if(a==7){
           that.dice_n17=that.dice_c1
         }else if(a==8){
           that.dice_n18=that.dice_c1
         }
         that.player1_index=a
         wx.request({
         url: 'http://192.168.43.236:8000/api/point/',
         data: {my_chess: this.player1_chess, enemy_chess: this.player2_chess, dice: this.dice_1, index: this.player1_index},
         method: 'POST',
         success: function(res) {
         console.log(res);
         that.point_1 = res.data.my_point;
         that.point_2 = res.data.enemy_point;
         that.column_point_11 = res.data.my_col1_point;
         that.column_point_12 = res.data.my_col2_point;
         that.column_point_13= res.data.my_col3_point;
         that.column_point_21 = res.data.enemy_col1_point;
         that.column_point_22 = res.data.enemy_col2_point;
         that.column_point_23 = res.data.enemy_col3_point;
         that.player1_chess = res.data.my_chess;
         that.player2_chess = res.data.enemy_chess;
         that.gameover = res.data.status;
         if (res.data.winner == 'my'){
           that.winner = 'player1';
           that.loser = 'player2';
         }
         else if (res.data.winner == 'enemy'){
           that.winner = 'player2';
           that.loser = 'player1';
         }
         else {
           that.winner = res.data.winner;
         }
         if (that.gameover == 1){
           that.$store.commit("getWinner",that.winner)
           that.$store.commit("getLoser",that.loser)
           if(that.winner=='player2')
           {
             that.$store.commit("getPoint_1",that.point_2)
             that.$store.commit("getPoint_2",that.point_1)
             that.$store.commit("getPlay1_url",that.user_url)
             that.$store.commit("getPlay2_url",that.robot_url)
             that.$store.commit("getPlay1_name",that.play2_name)
             that.$store.commit("getPlay2_name",that.play1_name)
           }else if(that.winner=='player1')
           {
             that.$store.commit("getPoint_1",that.point_1)
             that.$store.commit("getPoint_2",that.point_2)
             that.$store.commit("getPlay1_url",that.robot_url)
             that.$store.commit("getPlay2_url",that.user_url)
             that.$store.commit("getPlay1_name",that.play1_name)
             that.$store.commit("getPlay2_name",that.play2_name)
           }
           uni.navigateTo({
              url: '/subpkg/gameOver/gameOver'
              })
         }
         }
         })
         that.dice_c1='';
       },
       clickItem2(a){ 
          let that=this
          if(a==0)
          {
            that.dice_n20=that.dice_c2
          }else if(a==1){
            that.dice_n21=that.dice_c2
          }else if(a==2){
            that.dice_n22=that.dice_c2
          }else if(a==3){
            that.dice_n23=that.dice_c2
          }else if(a==4){
            that.dice_n24=that.dice_c2
          }else if(a==5){
            that.dice_n25=that.dice_c2
          }else if(a==6){
            that.dice_n26=that.dice_c2
          }else if(a==7){
            that.dice_n27=that.dice_c2
          }else if(a==8){
            that.dice_n28=that.dice_c2
          }
          that.player2_index=a
          wx.request({
          url: 'http://192.168.43.236:8000/api/point/',
          data: {my_chess: this.player2_chess, enemy_chess: this.player1_chess, dice: this.dice_2, index: this.player2_index},
          method: 'POST',
          success: function(res) {
          console.log(res);
          that.point_1 = res.data.enemy_point;
          that.point_2 = res.data.my_point;
          that.column_point_11 = res.data.enemy_col1_point;
          that.column_point_12 = res.data.enemy_col2_point;
          that.column_point_13= res.data.enemy_col3_point;
          that.column_point_21 = res.data.my_col1_point;
          that.column_point_22 = res.data.my_col2_point;
          that.column_point_23 = res.data.my_col3_point;
          that.player1_chess = res.data.enemy_chess;
          that.player2_chess = res.data.my_chess;
          that.gameover = res.data.status;
          if (res.data.winner == 'my'){
            that.winner = 'player2';
            that.loser = 'player1';
          }
          else if (res.data.winner == 'enemy'){
            that.winner = 'player1';
            that.loser = 'player2';
          }
          else {
            that.winner = res.data.winner;
          }
          that.dice_c2='';
          if (that.gameover == 1){
            that.$store.commit("getWinner",that.winner)
            that.$store.commit("getLoser",that.loser)
            if(that.winner=='player2')
            {
              that.$store.commit("getPoint_1",that.point_2)
              that.$store.commit("getPoint_2",that.point_1)
              that.$store.commit("getPlay1_url",that.user_url)
              that.$store.commit("getPlay2_url",that.robot_url)
              that.$store.commit("getPlay1_name",that.play2_name)
              that.$store.commit("getPlay2_name",that.play1_name)
            }else if(that.winner=='player1')
            {
              that.$store.commit("getPoint_1",that.point_1)
              that.$store.commit("getPoint_2",that.point_2)
              that.$store.commit("getPlay1_url",that.robot_url)
              that.$store.commit("getPlay2_url",that.user_url)
              that.$store.commit("getPlay1_name",that.play1_name)
              that.$store.commit("getPlay2_name",that.play2_name)
            }
            uni.navigateTo({
               url: '/subpkg/gameOver/gameOver'
               })
          }
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
      //padding-bottom: constant(safe-area-inset-bottom);
      //padding-bottom: env(safe-area-inset-bottom);
    }
  .local{
    width: 100%; 
    height: 100%;
  }
  .bg{
    position: absolute;
    z-index: 1;
  }
  .line{
    position: absolute;
    z-index: 1;
    width: 600rpx;
    height: 9rpx;
    border-top: 9rpx solid white;
    margin-top: 870rpx;
    margin-left: 80rpx;
  }
  .local_1{
    position: absolute;
    z-index: 2;
  }
  .p_n{
      display: flex;
      flex-direction:row;
  }
  .people{
    margin-left: 45rpx;
    margin-top: 140rpx;
    width: 160rpx;
    height: 160rpx;
    opacity: 1;
    border-radius: 10px;
    background: rgba(255, 255, 255, 1);
    
    border: 3px solid rgba(255, 195, 0, 1);            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    
  }
  .name{
    margin-top: 150rpx;
    width: 220rpx;
    height: 80rpx;
    opacity: 1;
    border-radius: 8px;
    background: rgba(233, 157, 66, 1);
    
    border: 3px solid rgba(252, 202, 0, 1);            
    /** 文本1 */
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: rgba(255, 255, 255, 1);
    text-align: center;
    line-height: 80rpx;
  }
  .point{
    margin-top: 240rpx;
    width: 90rpx;
    height: 80rpx;
    opacity: 1;      
    /** 文本1 */
    font-size: 90rpx;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
    text-align: center;
    line-height: 80rpx;
  }
  .place{
    margin-top: 160rpx;
    margin-left: 30rpx;
    width: 210rpx;
    height: 210rpx;
    opacity: 0.77;
    border-radius:0rpx 0rpx 0rpx 170rpx;
    border: 1px solid rgba(187, 187, 187, 1); 
    background: rgba(255, 255, 255, 1);    
  }
  .dice_1{
    position: fixed;
    margin-top: 160rpx;
    margin-left: 540rpx;
    z-index: 3;
    opacity: 1;
  }
  .touzi_1{
    position: absolute;
    z-index: 3;
  }
  .column_point_1{
    position: absolute;
    z-index: 3;
    width: 450rpx;
    height: 50rpx;
    margin-top: 450rpx;
    margin-left: 180rpx;
    display: flex;
    flex-direction:row;
    /** 文本1 */
    font-size: 50rpx;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
  }
  .column_point{
    width: 30%;
    text-align: center;
    
  }
  .local_2{
    position: absolute;
    margin-top: 1280rpx;
    z-index: 2;
  }
  .p_n_2{
      display: flex;
      flex-direction:row;
  }
  .people_2{
    
    margin-top: 140rpx;
    width: 160rpx;
    height: 160rpx;
    opacity: 1;
    border-radius: 10px;
    background: rgba(255, 255, 255, 1);
    
    border: 3px solid rgba(255, 195, 0, 1);            
    
    box-shadow: 0px 2px 6px 1px rgba(0, 0, 0, 0.25);
    
  }
  .name_2{
    margin-top: 200rpx;
    width: 220rpx;
    height: 80rpx;
    opacity: 1;
    border-radius: 8px;
    background: rgba(233, 157, 66, 1);
    
    border: 3px solid rgba(252, 202, 0, 1);            
    /** 文本1 */
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: rgba(255, 255, 255, 1);
    text-align: center;
    line-height: 80rpx;
  }
  .point_2{
    margin-top: 150rpx;
    width: 90rpx;
    height: 80rpx;
    opacity: 1;      
    /** 文本1 */
    font-size: 90rpx;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
    text-align: center;
    line-height: 80rpx;
  }
  .place_2{
    margin-top: 130rpx;
    width: 210rpx;
    height: 210rpx;
    opacity: 0.77;
    border-radius:0rpx 170rpx 0rpx 0rpx;
    border: 1px solid rgba(187, 187, 187, 1); 
    background: rgba(255, 255, 255, 1);    
  }
  .dice_2{
    position: fixed;
    margin-top: 1460rpx;
    margin-left: 0rpx;
    z-index: 3;
    opacity: 1;
  }
  .touzi_2{
    position: absolute;
    z-index: 3;
  }
  .column_point_2{
    position: absolute;
    z-index: 3;
    width: 450rpx;
    height: 50rpx;
    margin-top: 925rpx;
    margin-left: 180rpx;
    display: flex;
    flex-direction:row;
    /** 文本1 */
    font-size: 50rpx;
    font-weight: 600;
    letter-spacing: 0px;
    line-height: 0px;
    color: #7B4716;
  }
  .play_1 {
        position: absolute;
        z-index: 4;
        margin-top: 380rpx;
        margin-left: 180rpx;
  			display: flex;
        flex-wrap: wrap;
        width: 400rpx;
        height: 400rpx;
        
        
  		}
 .play_2 {
        position: absolute;
        z-index: 4;
        margin-top: 980rpx;
        margin-left: 180rpx;
  			display: flex;
        flex-wrap: wrap;
        width: 400rpx;
        height: 400rpx;
        
  		}   
.item {
  			width: 30%;
  			height: 30%;
  			margin: 7rpx;
  			//text-align: center;
  			//line-height: 30%;
  			//font-size: 34rpx;
  			//background: url(../../static/img/y_bg.jpg) no-repeat;
       
  			background-size: 100% 100%;
  			opacity:1;
  		}
</style>