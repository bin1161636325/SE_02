import  Vue from 'vue'
import  Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state:{
    winner:"",
    loser:"",
    point_1:0,
    point_2:0,
    user_url:'',
    user_name:'',
    play1_url:'',
    play2_url:'',
    play1_name:'',
    play2_name:'',
    other_name:'',
    other_url:'',
    first:0,
  },
  mutations:{
    getFirst:(state,data)=>{
      state.first=data;
    },
    getOther_name:(state,data)=>{
      state.other_name=data;
    },
    getOther_url:(state,data)=>{
      state.other_url=data;
    },
    getPlay1_name:(state,data)=>{
      state.play1_name=data;
    },
    getPlay2_name:(state,data)=>{
      state.play2_name=data;
    },
    getPlay1_url:(state,data)=>{
      state.play1_url=data;
    },
    getPlay2_url:(state,data)=>{
      state.play2_url=data;
    },
    getUser_url:(state,data)=>{
      state.user_url=data;
    },
    getUser_name:(state,data)=>{
      state.user_name=data;
    },
    getWinner:(state,data)=>{
      state.winner=data;
    },
    getLoser:(state,data)=>{
      state.loser=data;
    },
    getPoint_1:(state,data)=>{
      state.point_1=data;
    },
    getPoint_2:(state,data)=>{
      state.point_2=data;
    },
  },
  actions:{
    
  },
  getters:{
    // userName:(state)=>state.username
  }
})


export default store
