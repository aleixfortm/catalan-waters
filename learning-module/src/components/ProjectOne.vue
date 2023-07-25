<template>
    <div id="friend-1" v-if="visible1">{{friendOne}}</div>
    <div id="friend-2" v-if="visible2">{{friendTwo}}</div>
    <div id="friend-3" v-if="visible3">{{friendThree}}</div>
</template>
<script>
    export default {
        data() {
            return {
                friendOne: "Aleix",
                friendTwo: "Guillem",
                friendThree: "Pau",
                visible1: true,
                visible2: true,
                visible3: true
            }
        },
        methods: {
            makeItVisible() {
                var ranNum = Math.random() < 0.5 ? true : false;
                this.visible1 = ranNum;
                if (this.visible1 === true) {
                    this.friendOne = "Carles";
                }
                ranNum = Math.random() < 0.5 ? true : false;
                this.visible2 = ranNum;
                ranNum = Math.random() < 0.5 ? true : false;
                this.visible3 = ranNum;
            }
        },
        mounted() {
            this.makeItVisible();
            console.log(this.visible1);
            console.log(this.visible2);
            console.log(this.visible3);
        }
    }
</script>