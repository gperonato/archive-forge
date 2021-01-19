<template>
  <div>
    <h2>Archive-Forge</h2>

    <section class="form">
      <b-field label="Author of data generation">
        <b-input placeholder="ORCID" :value="author_orcid"></b-input>
        <b-input placeholder="First name" :value="first_name"></b-input>
        <b-input placeholder="Last name" :value="last_name"></b-input>
      </b-field>

      <b-field label="Related publication">
        <b-input placeholder="DOI" :value="pub_doi"></b-input>
      </b-field>
    </section>

    <div v-for="ds in dataset_items" :key="ds.ix" v-show="!isDownloading">
      <section class="form mt-5">
        <h3>{{ ds.ix+1 }}</h3>
        <DatasetForm :name="ds.name" :identifier="ds.id" />
      </section>
    </div>

    <div class="field has-text-centered m-5" v-show="!isDownloading">
      <button class="button is-primary m-2" @click="addDataset">+ Add dataset</button>
      <button class="button is-success m-2 fett" @click="useForge"><span>砧</span> Use the Forge!</button>
      <a target="_blank" href="https://www.youtube.com/watch?v=S1qK_TA52e4">
        <button class="button is-danger m-2">Upload to Zenodo</button>
      </a>
    </div>

    <section class="confirm m-5" v-show="isDownloading">
      <h2>&#x1F389; Woo hoo!</h2>
      <p>Your FAIR data archive is ready:</p>
      <button class="button is-default m-2" @click="cancelForge">Go back</button>
      <a href="#" download>
        <button class="button is-success is-large">
          &blacktriangledown; Download ZIP
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
import DatasetForm from "./DatasetForm";
const {Package} = require('datapackage')

export default {
  name: "ArchiveForge",
  props: {
    chan: String,
  },
  components: {
    DatasetForm,
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      author_orcid: "",
      pub_doi: "",
      users: "",

      dataset_items: [
        { ix: 0, id: "", name: "" }
      ],

      isDownloading: false,
      isErrored: false,
    };
  },
  methods: {
    addDataset () {
      let next = this.dataset_items.length
      this.dataset_items.push(
        { ix: next, id: "", name: "" }
      )
    },
    async useForge () {
      this.isDownloading = true;

      // Generate a data package
      console.log("Generating package ...")

      const descriptor = {
        resources: [
          {
            name: 'example',
            profile: 'tabular-data-resource',
            data: [
              ['height', 'age', 'name'],
              ['180', '18', 'Tony'],
              ['192', '32', 'Jacob'],
            ],
            schema:  {
              fields: [
                {name: 'height', type: 'integer'},
                {name: 'age', type: 'integer'},
                {name: 'name', type: 'string'},
              ],
            }
          }
        ]
      }

      const dataPackage = await Package.load(descriptor)
      const resource = dataPackage.getResource('example')
      resource.read().then((d) => {
        console.log(d);
        this.pub_doi = "12345"
      })
    },
    cancelForge () {
      this.isDownloading = false;
    },
    getCertified () {
      // build download link
      /*
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
        */
    },
  },
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.preview img {
  width: 200px;
}
h3 {
  margin: 0px;
  padding: 0px;
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
button.fett {
  font-weight: bold;
  font-size: 125%;
  text-shadow: 0 0 3px black;
}
.fett span {
  text-shadow: none;
  margin-right: 1em;
  color: rgba(0,0,0,0.2);
}
</style>
