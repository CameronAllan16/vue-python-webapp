<script lang="ts">
export default {
    props: ['message'],
};
</script>
<template>
    <div>
        <div class="alert alert-success" role="alert"> {{ message }}</div>
        <br />
    </div>

</template>