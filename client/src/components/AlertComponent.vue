<script lang="ts">
export default {
    props: ['message'],
};
</script>
<template>
    <div class="alert alert-warning alert-dismissable fade show" role="alert">
        {{ message }}
        <button type="button" class="close" data-dismiss="alert" aria-label="close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>

</template>