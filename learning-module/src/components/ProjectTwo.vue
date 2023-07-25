<template>
    <button @click="addNumber" class="add">Add</button>
    <div>{{number}}</div>
    <button @click="removeNumber" class="remove">Remove</button>
</template>
<script>
    export default {
        data() {
            return {
                number: 0
            }
        },
        methods: {
            addNumber() {
                this.number ++;
            },
            removeNumber() {
                
                if (this.number > 0) {
                    this.number --;
                }
            }
        }
    }
</script>