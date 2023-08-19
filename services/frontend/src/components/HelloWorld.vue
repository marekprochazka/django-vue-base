<template>
  <div>
    <h1>Hi test {{ props.msg }}</h1>
    <img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Big_fat_pig_with_tongue_out_in_Laos.jpg/1024px-Big_fat_pig_with_tongue_out_in_Laos.jpg"
        alt="pig">
  </div>
</template>


<script setup lang="ts">
import type {IHelloProps} from "@/components/props";

const props = defineProps<IHelloProps>()
</script>