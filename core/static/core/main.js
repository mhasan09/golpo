var getStatus = {
  data() {
    return {
      message: ""
    }
  },
  methods: {
    submitData() {
      var aa = this.message
      alert(aa)
  }
}
}

Vue.createApp(getStatus).mount('#status')



// var Counter = { 
//   data() {
//     return {
//       message: ""
//     }
//   },
//   methods: {
//     submitBid() {
//       var xx = this.message
     
      
//     },
//   },
// }


// Vue.createApp(Counter).mount('#root')
