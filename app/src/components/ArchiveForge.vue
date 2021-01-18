<template>
  <div>
    <section class="form">
      <h2>Archive-Forge</h2>

      <b-field label="Author of data generation">
        <b-input placeholder="ORCID"></b-input>
        <b-input placeholder="First name"></b-input>
        <b-input placeholder="Last name"></b-input>
      </b-field>

      <b-field label="Related publication">
        <b-input placeholder="DOI"></b-input>
      </b-field>
    </section>
    <hr />
    <section class="columns form">
      <div class="column is-one-half">
        <b-field label="Dataset name">
          <b-input placeholder="code-123"></b-input>
        </b-field>
      </div>
      <div class="column is-one-quarter">
        <div class="preview box" style="display: inline-block">
          Structure file
          <br /><small>(CSV, JSON, STL)</small>
        </div>
      </div>
      <div class="column is-one-quarter">
        <div class="preview box" style="display: inline-block">
          Data archive
          <br /><small>(ZIP)</small>
        </div>
      </div>
    </section>

    <div class="field has-text-centered m-5">
      <button class="button is-primary">+ Add dataset</button>
      <button class="button is-success">Use the Forge!</button>
    </div>

    <section class="confirm m-5" v-show="isDownloading">
      <h2>&#x1F389; Woo hoo!</h2>
      <p>Your FAIR data archive is ready:</p>
      <a :href="downloadUrl" download>
        <button class="button is-success is-large">
          &blacktriangledown; Download PDF
        </button></a
      >
    </section>

    <section class="confirm" v-show="isErrored">
      <b-notification type="is-warning" :closable="false">
        There was an error. Contact the developers
        <a :href="chan" target="_blank">for support</a>
        if you continue having an issue.
      </b-notification>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArchiveForge",
  props: {
    chan: String,
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      honestyPolicy: false,
      isDownloading: false,
      downloadUrl: null,
      previewUrl: null,
      isErrored: false,
      mailTo: null,
    };
  },
  methods: {
    getCertified: function () {
      // build download link
      this.downloadUrl = [
        this.first_name.trim(),
        this.last_name.trim(),
        ".pdf",
      ].join("");
      this.downloadUrl = [this.src, this.downloadUrl].join("/");
      // check if the link resolves
      this.isErrored = false;
      let confetti = this.$confetti;
      axios
        .get(this.downloadUrl)
        .then(() => {
          // replace form with confirmation
          this.isDownloading = true;
          confetti.start({
            particlesPerFrame: 0.5,
          });
          setTimeout(function () {
            confetti.stop();
          }, 5000);
        })
        .catch(() => {
          // show error message
          this.isErrored = true;
        });
    },
  },
  mounted() {
    this.previewUrl = this.src + "/preview.png";
    this.mailTo = "mailto:" + this.email + "?subject=Certificate";
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.preview img {
  width: 200px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
