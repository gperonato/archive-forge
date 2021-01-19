<template>
  <uploader :options="options" class="uploader-example">
    <uploader-unsupport></uploader-unsupport>
    <uploader-drop>
      <p>{{ label }}</p>
      <uploader-btn v-show="afile"
        >Select file</uploader-btn>
      <uploader-btn v-show="image" :attrs="attrs"
        >Select image</uploader-btn>
      <uploader-btn v-show="folder" :directory="true"
        >Select folder</uploader-btn>
    </uploader-drop>
    <uploader-list></uploader-list>
  </uploader>
</template>

<script>
export default {
  name: "UploadField",
  props: {
    label: String,
    types: String,
    image: { type: Boolean, default: false },
    folder: { type: Boolean, default: false },
  },
  data() {
    return {
      afile: !this.image && !this.folder,

      options: {
        testChunks: false,
      },
      attrs: {
        accept: "image/*",
      },
    };
  },
};
</script>

<style>
.uploader-example {
  width: auto;
  padding: 15px;
  font-size: 12px;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.4);
}
.uploader-example .uploader-btn {
  margin-right: 4px;
}
.uploader-example .uploader-list {
  max-height: 440px;
  overflow: auto;
  overflow-x: hidden;
  overflow-y: auto;
}
</style>
