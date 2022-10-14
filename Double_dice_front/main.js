import App from './App'
import 'animate.css';
// #ifndef VUE3
import Vue from 'vue'
import store from '@/store/index.js';
Vue.prototype.$store = store
Vue.config.productionTip = false
//http://192.168.43.236:3001/a.txt
import { $http } from '@escook/request-miniprogram'

import cuCustom from 'colorui/components/cu-custom.vue'
Vue.component('cu-custom',cuCustom)

import music from '@/utils/music.js'
// 挂载到vue实例上
Vue.prototype.$music =music 


uni.$http = $http
// 配置请求根路径
$http.baseUrl = 'http://192.168.43.236:3001'

// 请求开始之前做一些事情
$http.beforeRequest = function (options) {
  uni.showLoading({
    title: '数据加载中...',
  })
}

// 请求完成之后做一些事情
$http.afterRequest = function () {
  uni.hideLoading()
}
Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
    ...App,
    store
})
app.$mount()
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif