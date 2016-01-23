# fly

fly is an automated flyer/poster maker that works on Python and PIL.


#### Requirements

1. [PIL](http://pillow.readthedocs.org/en/3.0.x/installation.html)
2. arial.ttf
  1. Download from [here](https://github.com/JotJunior/PHP-Boleto-ZF2/raw/master/public/assets/fonts/arial.ttf)
  2. Copy it to /usr/share/fonts/truetype

#### Installation

`git clone https://github.com/ChennaiAstronomyClub/fly`

cd into the fly directory and do
`python setup.py install`

#### Usage

```
import fly
flyer = fly.ISS()
flyer.fly("Message Here")
```
#### Sample

![Sample](iss1453568747.jpg)

Functionality will be extended in the coming days to cover all our events. The following are the targets that are aimed to be covered.

- [x] ISS passes with [mercury](https://github.com/ChennaiAstronomyClub/mercury)
- [ ] Star Party invites
- [ ] Rocket Launch invites
- [ ] Monthly Meetup invites
- [ ] Outreach posters

#### License

MIT © [Chennai Astronomy Club](http://chennaiastronomyclub.org)