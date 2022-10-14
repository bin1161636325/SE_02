// pages/double_dice/double_dice.js
var socket = null; //全局定义socket对象
Page({
  /**
  * ⻚⾯的初始数据
  */
  data: {
  first:0,
  user_name:"星星",
  user_phone:"1846612541",
  user_picture_url:"",
  user_point:135,
  player1_chess:[0,0,0,0,0,0,0,0,0],
  player2_chess:[0,0,0,0,0,0,0,0,0],
  dice_1:0,
  dice_2:0,
  player1_index:0,
  player2_index:0,
  player1_point:0,
  player1_col1_point:"",
  player1_col2_point:"",
  player1_col3_point:"",
  player2_point:0,
  player2_col1_point:"",
  player2_col2_point:"",
  player2_col3_point:"",
  result: [],
  gameover: 0,
  winner: "",
  },
  /**
  * 决定先⼿
  */
  Gofirst: function(){
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/gofirst/',
  data: {},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.first = res.data.first;
  // console.log(that.data.first)
  }
  })
  },
  /**
  * player1随机骰⼦
  */
  Rolldice1: function(){
  let that = this;
  wx.request({
  url: 'http://192.168.43.9:8000/api/rolldice/',
  data: {},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.dice_1 = res.data.dice;
  // console.log(that.data.dice);
  }
  })
  },
  /**
  * player2随机骰⼦
  */
  Rolldice2: function(){
  let that = this;
  wx.request({
  url: 'http://192.168.43.9:8000/api/rolldice/',
  data: {},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.dice_2 = res.data.dice;
  // console.log(that.data.dice);
  }
  })
  },
  /**
  * player1点击盒⼦，把骰⼦放进去，分数计算, 包括列, 总分数, 消除后, 以及判断是否胜利
  */
  Point1: function(){
  console.log(this.data.player1_chess, this.data.player2_chess);
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/point/',
  data: {my_chess: this.data.player1_chess, enemy_chess: this.data.player2_chess, dice: this.data.dice_1, index: 
 this.data.player1_index},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.player1_point = res.data.my_point;
  that.data.player2_point = res.data.enemy_point;
  that.data.player1_col1_point = res.data.my_col1_point;
  that.data.player1_col2_point = res.data.my_col2_point;
  that.data.player1_col3_point = res.data.my_col3_point;
  that.data.player2_col1_point = res.data.enemy_col1_point;
  that.data.player2_col2_point = res.data.enemy_col2_point;
  that.data.player2_col3_point = res.data.enemy_col3_point;
  that.data.player1_chess = res.data.my_chess;
  that.data.player2_chess = res.data.enemy_chess;
  }
  })
  },
  /**
  * player2点击盒⼦，把骰⼦放进去，分数计算, 包括列, 总分数, 消除后, 以及判断是否胜利
  */
  Point2: function(){
  console.log(this.data.player1_chess, this.data.player2_chess);
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/point/',
  data: {my_chess: this.data.player2_chess, enemy_chess: this.data.player1_chess, dice: this.data.dice_2, index: 
 this.data.player2_index},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.player2_point = res.data.my_point;
  that.data.player1_point = res.data.enemy_point;
  that.data.player2_col1_point = res.data.my_col1_point;
  that.data.player2_col2_point = res.data.my_col2_point;
  that.data.player2_col3_point = res.data.my_col3_point;
  that.data.player1_col1_point = res.data.enemy_col1_point;
  that.data.player1_col2_point = res.data.enemy_col2_point;
  that.data.player1_col3_point = res.data.enemy_col3_point;
  that.data.player2_chess = res.data.my_chess;
  that.data.player1_chess = res.data.enemy_chess;
  }
  })
  },
  /**
  * ⼈机下⼀步
  */
  Ainextstep: function(){
  console.log(this.data.player2_chess, this.data.player1_chess, this.data.dice_2);
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/ainextstep/',
  data: {my_chess: this.data.player2_chess, enemy_chess: this.data.player1_chess, dice: this.data.dice_2},
  method: 'POST',
  success: function(res) {
  console.log(res);
  that.data.player2_point = res.data.my_point;
  that.data.player1_point = res.data.enemy_point;
  that.data.player2_col1_point = res.data.my_col1_point;
  that.data.player2_col2_point = res.data.my_col2_point;
  that.data.player2_col3_point = res.data.my_col3_point;
  that.data.player1_col1_point = res.data.enemy_col1_point;
  that.data.player1_col2_point = res.data.enemy_col2_point;
  that.data.player1_col3_point = res.data.enemy_col3_point;
  that.data.player2_chess = res.data.my_chess;
  that.data.player1_chess = res.data.enemy_chess;
  }
  })
  },
  /**
  * 点击排行榜
  */
  Rankinglist: function(){
  console.log(this.data.user_name, this.data.user_phone, this.data.user_picture_url, this.data.user_point);
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/rankinglist/',
  data: {player_name: this.data.user_name, player_picture_url: this.data.user_picture_url, player_phone: this.data.user_phone},
  method: 'POST',
  success: function(res) {
  console.log(res);
  }
  })
  },
  /**
  * 添加记录
  */
  Addrank: function(){
  console.log(this.data.user_name, this.data.user_phone, this.data.user_picture_url, this.data.user_point);
  let that = this;
  wx.request({
  url: 'http://192.168.43.236:8000/api/addrank/',
  data: {player_name: this.data.user_name, player_picture_url: this.data.user_picture_url, player_phone: this.data.user_phone, player_point: this.data.user_point},
  method: 'POST',
  success: function(res) {
  console.log(res);
  }
  })
  },
  onLoad(options) {
    var that = this;
    // 创建websocket
    // 正式地址使用wss
    socket = wx.connectSocket({
        url: 'ws://192.168.43.236:8000/room/' + '123' + '/',
        success: function(res) {
            console.info('创建连接成功');
            //socketTaskId: 22
            // console.info(res);
        }
    });
    // console.info(socket);
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
    // 服务器发送监听
    // 服务器发送过来做出反应
    socket.onMessage(function(res) {
        console.info(res);
        var data = res.data;
        console.log(data)
        var json = JSON.parse(data);
        if (json.dice_1 != undefined){
          console.log(json.dice_1)
          that.data.dice_1 = json.dice_1
        }
        else if (json.dice_2 != undefined){
          console.log(json.dice_2)
          that.data.dice_2 = json.dice_2
        }
        else if (that.data.dice_1 > 0){
          console.log(json.my_chess, json.enemy_chess)
          that.data.player1_chess = json.my_chess
          that.data.player2_chess = json.enemy_chess
          that.data.player1_col1_point = json.my_col1_point
          that.data.player1_col2_point = json.my_col2_point
          that.data.player1_col3_point = json.my_col3_point
          that.data.player2_col1_point = json.enemy_col1_point
          that.data.player2_col2_point = json.enemy_col2_point
          that.data.player2_col3_point = json.enemy_col3_point
          that.data.gameover = json.status
          that.data.winner = json.winner
          that.data.dice_1 = 0
        }
        else if (that.data.dice_2 > 0){
          console.log(json.my_chess, json.enemy_chess)
          that.data.player1_chess = json.enemy_chess
          that.data.player2_chess = json.my_chess
          that.data.player1_col1_point = json.enemy_col1_point
          that.data.player1_col2_point = json.enemy_col2_point
          that.data.player1_col3_point = json.enemy_col3_point
          that.data.player2_col1_point = json.my_col1_point
          that.data.player2_col2_point = json.my_col2_point
          that.data.player2_col3_point = json.my_col3_point
          that.data.gameover = json.status
          that.data.winner = json.winner
          that.data.dice_2 = 0
        }
    });
  },
  // 发送player_1骰子事件，求返回值为骰子数
  sendRolldice1() {
    socket.send({
        data: "dice_1",
        success: function(res) {
            console.info('player_1骰子事件发送成功');
        }
    });
  },
  // 发送player_2骰子事件，求返回值为骰子数
  sendRolldice2() {
    socket.send({
        data: "dice_2",
        success: function(res) {
            console.info('player_2骰子事件发送成功');
        }
    });
  },
  // 发送player_1下棋事件，求返回值为棋盘
  sendPoint1() {
    socket.send({
        data: JSON.stringify({my_chess: this.data.player1_chess, enemy_chess: this.data.player2_chess, dice: this.data.dice_1, index: this.data.player1_index}),
        success: function(res) {
            console.info('player_1下棋事件发送成功');
        }
    });
  },
  // 发送player_2下棋事件，求返回值为棋盘
  sendPoint2() {
    socket.send({
        data: JSON.stringify({my_chess: this.data.player2_chess, enemy_chess: this.data.player1_chess, dice: this.data.dice_2, index: this.data.player2_index}),
        success: function(res) {
            console.info('player_2下棋事件发送成功');
        }
    });
  },
  /**
  * ⽣命周期函数--监听⻚⾯初次渲染完成
  */
  onReady() {
  },
  /**
  * ⽣命周期函数--监听⻚⾯显示
  */
  onShow() {
  },
  /**
  * ⽣命周期函数--监听⻚⾯隐藏
  */
  onHide() {
  },
  /**
  * ⽣命周期函数--监听⻚⾯卸载
  */
  onUnload() {
  },
  /**
  * ⻚⾯相关事件处理函数--监听⽤户下拉动作
  */
  onPullDownRefresh() {
  },
  /**
  * ⻚⾯上拉触底事件的处理函数
  */
  onReachBottom() {
  },
  /**
  * ⽤户点击右上⻆分享
  */
  onShareAppMessage() {
  }
 })