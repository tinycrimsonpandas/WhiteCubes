# WhiteCubes

A (hopefully) easy way to produce a simple static gallery site for visual artists. Many people use Squarespace or Wix and they end up with sites that look like a webstore, instead WhiteCubes hopes to provide a simple and minimal design focused on presnting art and text easily. This was inspired by the (Indexibit)[https://indexhibit.org] project and tries to recreate the feel of that project without needing a database and more expensive hosting. This was created as a final project for Harvard's CS50.

Built on flask, frozen flask, flask flatpages, and netlify cms. Easily deployable to Netlify's platform for static sites. For most people (those with less than 100GB of bandwith usage a month), this software should enable a simple porfolio site for only the yearly cost of a custom domain name. 

Here is an example site, the original inspiration for this project (currently under construction):
[Example!](https://amazing-euler-31dfc1.netlify.app)

## Features
* 15 dollars a year (or cheaper depending on TLD) compared to 15 dollars a month at Squarespace etc.
* Simple UI to create galleries (collections of images) and pages (text or HTML content)
* Built-in slideshow/lightbox on every gallery page
* Built-in automatic image resizing and thumbnail generation
* Create pages easily using markdown or HTML


***

## Installation

### Easiest Method

1. First deploy this repo to netlify by clicking this button -->
<a href="https://app.netlify.com/start/deploy?repository=https://github.com/tinycrimsonpandas/WhiteCubes"><img src="https://www.netlify.com/img/deploy/button.svg" alt="Deploy to Netlify"></a>

2. Once the initial deploy is successful, set yourself up a user account on your new Netlify site by navigating to the Identity tab, clicking "Enable Identity", then "Invite Users" to add yourself as a user! Follow the instructions in your email to activate your account. **Make sure to turn off registrations by going to Identity settings, under the "Registration Preferences" section clicking "Edit Settings" then selecting "Invite Only" then click "Save". If you don't then you could allow anyone to edit your site.**

3. Once your account is activated, go to `[temporary url from netlify]/static/admin/` and log in using the credentials you just created.

4. Go to the 'Settings' collection in the control panel and first set-up your sitewide settings (including site title, instagram link, default open graph image, etc).

6. Start adding galleries and pages (see below for more information). 

6. Eventually, buy or point your custom domain to Netlify and configure it for your new site. [More info here.](https://docs.netlify.com/domains-https/custom-domains/configure-external-dns/#configure-a-subdomain)

### Harder

#### Requirements
* Python 3.7+
* pipenv (install by running `pip3 install pipenv`)

#### Steps

1. Clone this repo locally, then `cd` into the cloned directory

2. Run `pipenv install` in the cloned directory

2. Edit the site config at `settings/site.yml` file with your new site title, instagram links, etc.

3. Adjust the Netlify CMS panel config file (located at `static/admin/config.yml`) to match your preferred backend and authentication method. [Click here](https://www.netlifycms.org/docs/backends-overview/) for more information. You can also skip this step and just create pages using a text editor. The wiki of this repo includes information on the file format and directory structure. 

4. Run `pipenv shell` to access the virtual envrionment of your site.

5. Run `python whitecube.py` to create your static site, which will appear in the new `/build` directory.

6. Optionally you can run `python whitecube.py preview` to build the site and then launch a local flask server to preview your static content. Please note that you are previewing the statically generated content, so any edits require re-running `pythong whitecube.py preview`. There is one limitation with the preview mode: you cannot see your custom error pages.

7. Set up your static server of your choice, such as GitHub Pages, any manually upload the build folder or set up a CI/CD process of your preference.

***

## Usage

### Creating Galleries and Pages

Instead of using a database, WhiteCubes uses a file-based system to store your galleries and posts. The format for the files are described [in the wiki](https://github.com/tinycrimsonpandas/WhiteCubes/wiki/Page-and-Gallery-File-Format).

You can either create and edit galleries and pages using a text editor of your choice and then by either building the static site yourself as desribed above OR by using the Netlify CMS control panel that is configured for these file formats. 

#### Using the Netlify CMS to Manage Galleries and Pages

Make sure you've set up Netlify CMS using the information described above. Once you've done that the creation of pages is easy. Simply navigate to `[your site url]/static/admin` and login using the credentials you set up. 

Once you log in you will see a sidebar labeled **Collections** that will have three options: _Pages, Galleries, Settings_.

To create a gallery or page, click on the appropriate link in the sidebar and then click either **New Page** or **New Gallery**, enter the content you'd like to make, then click **Publish**. This will automatically make a new commit to your linked repository and if you're using Netlify's platform or another CI/CD integration you set up yourself will automatically start rebuilding and publishing your update site. 

#### Reverting Changes

If you publish a mistake, you can edit it using the interface or by editing the text files directly. You can also simply revert the commit made to the git repository that is linked to your site and revert to a previous version of the site. 

### Adjusting the Nav Bar

Like the galleries and posts, the navigation bar contents are also stored in a file located at `settings/nav.yml`. _Further information about all of the configuration files can be [found in the wiki](https://github.com/tinycrimsonpandas/WhiteCubes/wiki/Configuration-Files)._

#### Using Netlify CMS to Edit the Navigation Bar

Make sure you've set up Netlify CMS using the information described above. Once you've done that the creation of pages is easy. Simply navigate to [your site url]/static/admin and login using the credentials you set up.

Once logged in, navigate to the **Settings** collection then click on **Navigation**. 

From there you will see two boolean options:
* **Display index link?** - allows you to choose whether or not the site title and link to the homepage is displayed in the navbar
* **Display instagram link?** - allows you to chose whether or not an instagram icon is displayed at the bottom of the navbar. The instagram URL is set in the **Site Settings** configuration file. 

Following these two options you will be able to add individual navigiation items. At the moment you can have an assortment of two items: **Line Spaces** and **Nav Links**. 

* **Line Spaces** create a gap in the navigation bar
* **Nav Links** have two fields. _Link Text_ which defines the string that will be displayed in the Navigation Bar and _Link_ which is the path to the item you'd like to link to. In the future the system will differentiate between internal and external links and allow you to select easily pages and galleries you've created, but at the moment you have to enter the URL yourself. 




