<!--
            BEFORE YOU MAKE CHANGES
            - please put them in the correct section
            - sections are __consistent__ across apps
-->

<!-- ASCII ART HERE -->
[![Build Status](https://job_url/badge/icon)](https://job_url/)

Brief description about this service

For more information about this service: <a href="">Link To Wiki</a>

# Table Of Contents #

* [Important Links](#env-build)
* [Installing](#installing)
 * [Config](#installing-config)
 * [Dependencies](#installing-dependencies)
* [Running](#running)
* [Developing](#developing)
 * [Conventions](#developing-conventions)
* [Testing](#testing)
 * [Types of Tests](#testing-types)
 * [Running Tests](#testing-running)
* [Pull Requests](#pullrequest)
 * [Trigger Phrases](#pullrequest-trigger-phrases)
* [Build & Releasing](#releasing)
 * [RC](#releasing-rc)
 * [Production](#releasing-production)
* [Hot Fix](#hot-fix)

- - -
## <a name="env-build"></a>Important Links
coming soon

- - -
## <a name="installing"></a>Installing

```bash
git clone git@github.2ndsiteinc.com:dev/business_lookup.git
cd business_lookup
make install
```

This will create a virtualenv and install all the dependencies.

#### <a name="installing-config"></a>Configurations
coming soon

#### <a name="installing-dependencies"></a>Dependencies
*Updating Dependencies:*
If you have updated dependencies you'll need to rebuild the wheelhouse that business_lookup uses. Run the following

```bash
make wheelhouse
```

This will generate `.whl` files for all of business_lookup's dependencies and copy them to optimus. If you run this from
your dev machine, the `scp` command may fail. If this happens, re-run it from your host machine.

- - -
## <a name="running"></a>Running
###### In the background
coming soon

###### In the foreground

You can run business_lookup using make

```
make server
```

- - -
## <a name="developing"></a>Developing
#### <a name="developing-conventions"></a>Conventions
coming soon

- - -
## <a name="testing"></a>Testing
#### <a name="testing-types"></a>Types of Tests
unittest: PyUnit -- /test -- /test/cli (for CLI tests)

#### <a name="testing-running"></a>Running Tests
###### Running All Tests
You can run tests for business_lookup using `make test`. Alternatively, activate the virtualenv and run
`nosetests -s`.

###### Running Individual Tests
coming soon

- - -
## <a name="pullrequest"></a>Pull Requests
#### <a name="pullrequest-trigger-phrases"></a>Trigger Phrases
coming soon

- - -
## <a name="releasing"></a>Build & Releasing
When it is time to release business_lookup do the following:

1. Make all your changes.
2. Run `make tag VERSION=x.y.z`.
3. The `business_lookup+package` jenkins job will pick up the new tag and create an RPM.
4. The RPM will be put into `optimus.2ndsiteinc.com/packages/rpms/dev/business_lookup`.
5. Downstream jobs will automatically update the RC environment with the new package.
6. An ops ticket will be required to get business_lookup deployed to production.

#### <a name="releasing-rc"></a>To RC
coming soon

#### <a name="releasing-production"></a>To Production
coming soon

- - -
## <a name="hot-fix"></a>Hot Fix
coming soon

