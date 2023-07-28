<template>
    <button @click="addNumber" class="add">Add</button>
    <div>{{number}}</div>
    <button @click="removeNumber" class="remove">Remove</button>
    <br><br>

    <input placeholder="Insert your Name" v-model="username">
    <div>{{ username }}</div>
</template>
<script>
    export default {
        data() {
            return {
                number: 0,
                username: ''
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
            },
            printToConsole() {
                console.log(this.username);
            }
        },
        mounted() {
            this.printToConsole();
        }
    }
</script>