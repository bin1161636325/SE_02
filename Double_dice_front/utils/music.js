const bgm = uni.createInnerAudioContext();
bgm.src = 'https://bjetxgzv.cdn.bspapp.com/VKCEYUGU-hello-uniapp/2cc220e0-c27a-11ea-9dfb-6da8e309e0d8.mp3'
bgm.loop = true;

var music = {
    //mute 表示是否是静音，，默认不静音
    playBgm({mute=false}){
        if (!bgm) return;
        if(mute){
            bgm.pause()
        }else{
            bgm.play()
        }
        
        bgm.onPause(()=>{
            console.log('暂停背景音乐');
        })
        bgm.onPlay(() => {
            console.log('开始播放音乐#######');
        })
        bgm.onError((res) => {
            console.log(res)
        })
    }
}
module.exports = music
