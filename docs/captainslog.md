# BlindGumption Captain's Log

in here I'll be writing my thoughts on how to build BlindGumption.
It will be ostly high level ideas with bullet points listing steps I plan to take.
I thought about using github projects, and I might if anyone else starts working with me.
For now, it's easiest to keep goals and progress in one place.

## Step 0: New blindgumption repo

This is already done, but deserves some explanation.

I wanted a new start on BlindGumption.
I've thought a lot about what it should be, and whether I'm wasting my time.
I have somewhat of an idea on what it should be, at least initially.
Whether I'm wasting my time is an open question.

The original main-blindgumption repo was full of static HTML
with many elements duplicated across text files.
I'm not going to do that any more.
My plan is to build out BlindGumption using 
[domible](https://github.com/joeldodson/domible),
the package of Python classes I'm developing to render HTML documents and elements.
I'm starting this new leaf on BlindGumption in part to have a place to showcase domible.

### Monorepo

I currently have 4 domains for blindgumption: .com, .dev. .xyz, and .org.
blindgumption.com will be the main site and (should) be always up and functioning.
blindgumption.dev will serve as a staging site.
Anything destine for blindgumption.com will initially be deployed on blindgumption.dev.
Though, some apps might spend a long time on blindgumption.dev and maybe never be fully deployed.
blindgumption.xyz is a playground for ideas I'm bouncing around and want to expose to the public.
I'll post them on blindgumption.xyz to get feedback.
blindgumption.org is aspirational and could become anything, or nothing.

I thought about having separate repos for each domain,
and using git submodules.
After considering the various trade offs, I decided on a monorepo.
I didn't want to deal with the overhead of submodules and there will be shared code across the different domains.

The biggest downside to a monorepo seemed to be a likelihood
of it turning into spaghetti code and components that arguably should have been submodules
become tightly coupled.
Assuming I'll be the only developeer on BlindGumption for the foreseeable future,
there's no way that's going to happen.
Really, how often has any developer turned their pet project into a tightly coupled mess of undocumented hackery?

## Step 1: Documentation 

I find it helpful to write as I'm thnking and trying to organize my thoughts.
Thus, now that the repo is set, where and how to document this momentous occasion is the next logical step.

As you can see, There is a docs directory in the repo and a mkdocs.yml config file at the root.
I have also setup a github action to build and deploy these markdown files to the 
blindgumption repo's github pages upon a push to the main branch event.

I can update the Captain's Log whenever the urge strikes,
and can add new files by simply creating a new markdown file in the docs folder,
and adding it to the nav section in the mkdocs.yml file.

I'm calling Step 1 complete!

## Step 2: Infrastructure

Time to discuss what the BlindGumption platform will be initially.
First though, very briefly, what it was.

Initially, blindgumption.com was (and still is as I write this) 
deployed on a single droplet in DigitalOcean.
Static HTML files were being served by an Nginx reverse proxy.
It was fairly easy to setup given the great tutorials on DigitalOcean.
As already mentioned, the static HTML was full of duplicated elements (copy'n'paste).
I wanted a way to not duplicate text and make it easier to manage and extend the platform.
Here's how I plan to do that. 

###### end of CAPTAINSLOG