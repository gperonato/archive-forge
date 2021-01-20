<template>
  <div>
    <section class="form">
      <b-field label="Author of data generation">
        <b-input placeholder="First name" :value="first_name"></b-input>
        <b-input placeholder="Last name" :value="last_name"></b-input>
        <span class="middletext">or</span>
        <a href="https://info.orcid.org/documentation/features/public-api/reading-orcid-records/" target="_blank">💡</a>
        <b-input placeholder="ORCID" :value="author_orcid"></b-input>
      </b-field>

      <b-field label="Dataset name and title">
        <b-input placeholder="my-data-package" :value="dataset_name"></b-input>
        <b-input placeholder="My Data Package" :value="dataset_title"></b-input>
      </b-field>

      <b-field label="Publication and license">
        <b-input placeholder="Article DOI" :value="pub_doi"></b-input>
        <b-input placeholder="License" :value="pub_license"></b-input>
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
      <a :href="downloadUrl" download="datapackage.json">
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
      dataset_title: "",
      dataset_name: "",
      pub_license: "",
      pub_doi: "",
      users: "",
      downloadUrl: "",

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

      let descriptor = {
        name: this.dataset_name,
        title: this.dataset_title,
        description: "Generated with Archive Forge",
        licenses: [
          {
            "title": this.pub_license,
            "path": "http://opendefinition.org/licenses/"
          }
        ],
        "sources": [
          {
            "title": "Publication",
            "path": "https://doi.org/" + this.pub_doi,
          }
        ],
        profile: "tabular-data-package",
        resources: []
      }

      this.dataset_items.forEach(function(ds) {
        descriptor.resources.push(
          {
            name: ds.id,
            title: ds.name,
            profile: 'tabular-data-resource',
            data: [
              ['SMILES','NMREDATA_VERSION','NMREDATA_LEVEL'],
              ['69.5534', '3', '11008.6355'],
              ['72.6738', '1', '10482.8115'],
              ['92.0096', '4', '10125.3933'],
            ],
            schema:  {
              fields: [
                {
                  "format": "default",
                  "name": "SMILES",
                  "type": "string"
                },
                {
                  "format": "default",
                  "name": "NMREDATA_VERSION",
                  "type": "string"
                },
                {
                  "format": "default",
                  "name": "NMREDATA_LEVEL",
                  "type": "string"
                }
              ]
            }
          }
        )
      })
      console.log(descriptor)
      this.downloadUrl = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(descriptor));

      const dataPackage = await Package.load(descriptor)
      const resource = dataPackage.getResource('example')
      resource.read().then((d) => {
        this.downloadUrl = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(d));
      })
    },
    cancelForge () {
      this.isDownloading = false;
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
.middletext {
  margin: 0.5em;
}
</style>
