# doc-portal-prototype

Prototype for the Rubin documentation portal to explore the metadata schema and organizational strategy. For the Documentation Working Group.

This repository includes two key files:

- `metadata.yaml` is a YAML-formatted file that contains the *metadata* about a representative set of Rubin documentation resources. This metadata is what will power the documentation portal: metadata can be used for display purposes, to enable organization and navigation, or to enable search.

  Each array item in `metadata.yaml` is a separate, isolated, documentation resource.

- `schema.json` is the *schema* for `metadata.yaml`; a schema defines the expected and allowed shape of a dataset. As we determine what information needs to be associated with document's metadata record, we need to add those new fields to `schema.json`. The tests for this repository continuously check that `metadata.yaml` conforms to `schema.json`.

  The schema is written with [JSON Schema](https://json-schema.org). A great tutorial is available at [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/index.html).

Both of these files can become valuable resources for the Documentation Working Group: the `schema.json` file becomes a guide to what information needs to be collected to create a useful documentation portal experience, while `metadata.yaml` is a useful representative demo of the types of documentation we have that can power prototypes of the documentation portal.

## Working with this repository: a primer

*Working with this repository requires command line, Git and a GitHub account, and ideally a Python 3 installation as well.*

Clone this repository:

```sh
git clone https://github.com/lsst-sitcom/doc-portal-prototype
cd doc-portal-prototype
```

If you will be contributing changes, create a branch:

```sh
git checkout -b <branch-name>
```

Install the testing tools:

```sh
make init
```

Now, add a document to `metadata.yaml` or edit the schema in `schema.json`.
At any time you can ensure the metadata conforms to the schema:

```sh
make test
```

Commit any changes, for example:

```sh
git add -a
git commit
```

Note that the pre-commit tests run automatically at this point if you installed them (`make init`).
If these pre-commit hooks reformatted any files, you'll need to re-add those changes files with `git add` and then try `git commit` again.

You can create a new pull request on GitHub by running

```sh
git push -u
```

For more information about creating commits and pull requests, see the [GitHub documenation](https://docs.github.com/en/pull-requests).
