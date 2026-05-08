# DiVA REST API Examples

This repository contains examples to help get started with the DiVA REST API.

The .http files should be human readable so that you can copy the requests to your favourite REST Client.

Use can also use the REST Client extension for VSCode or another IDE that recognizes the .http file format, and you can interact with the API directly from the files.

## Getting started

### 1. Read and search public data (no authentication needed)

The `pre/` directory contains examples for the public API on the pre environment.

- [read-publication.http](pre/read-publication.http) — Read a single publication by ID
- [search-publications.http](pre/search-publications.http) — Search by title, DOI, or free text

The `Accept` header controls the response format:

- `application/vnd.cora.record+xml` or `+json` — standard format
- `application/vnd.cora.record-decorated+xml` or `+json` — includes linked records and field labels, useful for display

### 2. Authenticate (required for write operations)

The preview environment provides example users for testing. To get a token:

1. Fetch the deployment info to see available example users ([authenticate.http](preview/authenticate.http))
2. Log in with an example user's login ID and app token to receive an auth token
3. Include the token in subsequent requests via the `AuthToken` header

Tokens are short-lived (~10 minutes). Use the renew endpoint to extend a session without logging in again.

### 3. Create, update, and delete records

Once authenticated, you can use the token to modify records on preview:

- [createPublication.http](preview/createPublication.http) — Create a book publication
- [createPerson.http](preview/createPerson.http) — Create a person record
- [updatePublication.http](preview/updatePublication.http) — Update a publication (copy the record from create/read response and modify it)
- [deletePublication.http](preview/deletePublication.http) — Delete a publication by ID

## Environments

### Preview (https://preview.diva.cora.epc.ub.uu.se/rest)

This environment contains the latest changes that have been developed. The data will be wiped frequently, sometimes multiple times per day.

The environment contains example users that can be fetched via the deploymentInfo endpoint (See [authenticate.http](preview/authenticate.http)) which makes it a good environment to try and updating creating records

### Pre (https://pre.diva-portal.org)

This is a production-like environment that contains the latest migrated data. Functionality and data is refreshed less frequently than on preview. Roughly biweekly.

This environment only has real users and does not provide example users as preview does. Since it has production data it's a good environment to try the public, non-authenticated API by reading and searching data.
