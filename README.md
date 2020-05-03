# WhiteCubes

A (hopefully) easy way to produce a simple static gallery site for visual artists. Many people use Squarespace or Wix and they end up with sites that look like a webstore, this was inspired by the Indexibit project and tries to recreate the feel of that without needing a database and more expensive hosting. This was created as a final project for Harvard's CS50.

Built on flask, frozen flask, netlify cms, and easily deployable to Netlify's CI/CD platform for static sites. For most people (those with less than 100GB of bandwith usage a month), this software should enable a simple porfolio site for only the yearly cost of a custom domain name. 

## Benefits
* Super simple website generator for visual artists, deploy to netlify and then use the CMS interface to add galleries, pages, and even contact forms. 
    * Can be used without Netlify on any host capable of delivering HTML documents. Though the setup for the CMS control panel requires a couple extra steps
* Responsive and mobile ready
* Integrates OpenGraph and SEO tags

## Installation

### Easiest Method

1. First deploy this repo to netlify by clicking this button -->
<a href="https://app.netlify.com/start/deploy?repository=https://github.com/tinycrimsonpandas/WhiteCubes"><img src="https://www.netlify.com/img/deploy/button.svg" alt="Deploy to Netlify"></a>

2. Once the initial deploy is successful, set yourself up a user account on your new Netlify site by navigating to the Identity tab, clicking "Enable Identity", then "Invite Users" to add yourself as a user! Follow the instructions in your email to activate your account. 

3. Once your account is activated, go to `[temporary url from netlify]/static/admin/` and log in using the credentials you just created.

4. Go to the 'Settings' collection in the control panel and first set-up your site title, instagram link, default open graph image, etc.

6. Start adding galleries and pages (see below for more information). [More info here.](https://docs.netlify.com/domains-https/custom-domains/configure-external-dns/#configure-a-subdomain)

6. Eventually, buy or point your custom domain to Netlify and configure it for your new site. 

### Harder

#### Requirements
* Python 3.7+
* pipenv (install by running `pip3 install pipenv`)

#### Steps

1. Clone this repo locally, then `cd` into the cloned directory

2. Run `pipenv install` in the cloned directory

2. Edit the `site.yml` file with your new site title, instagram links, etc.

3. Adjust the Netlify CMS panel config to match your preferred backend and authentication. [Click here](https://www.netlifycms.org/docs/backends-overview/) for more information. You can also skip this step and just create pages using a text editor. The wiki of this repo includes information on the file format and directory structure. 

4. Run `pipenv shell` to access the virtual envrionment of your site.

5. Run `python whitecube.py` to create your static site, which will appear in the new `/build` directory.

6. Optionally you can run `python whitecube.py preview` to build the site and then launch a local flask server to preview your static content. Please note that you are previewing the statically generated content, so any edits require rerunning `pythong whitecube.py preview`. There is one limitation with the preview mode, currently you cannot see 

7. Set up your static server of your choice, such as GitHub Pages, any manually upload the build folder or set up a CI/CD process of your preference.


## Creating Galleries and Pages
COMING SOON 
