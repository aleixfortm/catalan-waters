<template>
    <input placeholder="Type your Name" v-model="name">
    <div :class="{ red: isHovered }" @mouseover="hovered" @mouseout="hoveredOut">{{ name }}</div>
</template>
<script>
export default {
    data() {
        return {
            name: '',
            isHovered: false
        }
    },
    methods: {
        hovered() {
            this.isHovered = true;
        },
        hoveredOut() {
            this.isHovered = false;
        }
    }
}
</script>
<style>
    .red {
        color: rgb(112, 0, 0);
        font-weight: bold;
    }
    .blue {
        color:rgb(0, 73, 73);
    }
</style>