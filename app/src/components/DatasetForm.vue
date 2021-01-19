<template>
  <div>
    <div class="columns mt-1">
      <div class="column is-one-half">
        <b-field label="Dataset name">
          <b-input placeholder="code-123" :v-model="name"></b-input>
        </b-field>
      </div>
      <div class="column is-one-half">
        <b-field label="Identifier">
          <b-input placeholder="Compound number/code" :v-model="identifier"></b-input>
        </b-field>
      </div>
    </div>

    <div class="columns mt-1">
      <div class="column is-one-third">
        <UploadField label="Structure file" types="csv,json,stl" />
      </div>
      <div class="column is-one-third">
        <UploadField label="Data archive" folder />
      </div>
      <div class="column is-one-third">
        <UploadField label="Visualization" image />
      </div>
    </div>
  </div>
</template>

<script>
import UploadField from "./UploadField";

export default {
  name: "DatasetForm",
  props: {
    name: String,
    identifier: String,
  },
  components: {
    UploadField,
  },
  data() {
    return {
    }
  },
};
</script>

<style>

</style>
