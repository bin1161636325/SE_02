const http = (url, data, methods) => {
  return new Promise(function (resolve, reject) {
    wx.request({
      url: `${url}`,
      method: `${methods}`,
      data: data,
      header: {
        'content-type': 'application/x-www-form-urlencoded', // 默认值
      },
      success: function (res) {
        if (res.statusCode != 200) {
          reject({ error: '服务器忙，请稍后重试', code: 500 });
          return;
        }
        resolve(res.data);
      },
      fail: function (res) {
        console.log(res)
        // fail调用接口失败
        reject({ error: '网络错误', code: 0 });
      }
    })
  })
}

module.exports = http