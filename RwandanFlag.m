% Rwandan flag
% Author: Rutaris
% Date: April 6th, 2014

clc; clf;clear all;

fxmin = 0;
fxmax = 20;
fymin = 0;
fymax = 15;

x = fxmax*4/5;
y = fymax*3/4;

rwblue = [38, 126, 224]/255;
rwyellow = [255, 255, 2]/255;
rwgreen = [85, 163, 62]/255;

bluebox = [fxmin, fymax; fxmin, fymax/2; fxmax, fymax/2; fxmax, fymax];
blueb = fill(bluebox(:,1), bluebox(:, 2), rwblue);
set(blueb,'edgecolor',rwblue);
hold on
yellowbox = [fxmin, fymax/2; fxmin, fymax/4; fxmax, fymax/4; fxmax, fymax/2];
yellowb = fill(yellowbox(:,1), yellowbox(:,2), rwyellow);
set(yellowb, 'edgecolor', rwyellow);

greenbox = [fxmin, fymax/4; fxmin, fymin; fxmax, fymin; fxmax, fymax/4];
greenb  = fill(greenbox(:,1), greenbox(:,2), rwgreen);
set(greenb, 'edgecolor', rwgreen);

r = (fymax*2/4)*0.34;
tang = 0:pi/24:2*pi;
tang(end) = [];
n = length(tang);
ht = 1/2;
vsx= zeros(n,1);
vsy= zeros(n,1);

for i = 1:n
    if mod(i, 2) ~= 0
        vsx(i) = r*cos(tang(i)) + x;
        vsy(i) = r*sin(tang(i)) + y;
    else
        vsx(i) = r*ht*cos(tang(i)) + x;
        vsy(i) = r*ht*sin(tang(i)) + y;
    end    
end

t = fill(vsx, vsy, rwyellow);
set(t,'edgecolor',rwyellow);

rc1 = (1-ht)*r*7/8;
xc1 = rc1*cos(tang) + x;
yc1 = rc1*sin(tang) + y;
c1 = fill(xc1, yc1, rwblue);
set(c1,'edgecolor',rwblue);

rc2 = rc1*7/8;
xc2 = rc2*cos(tang) + x;
yc2 = rc2*sin(tang) + y;
c2 = fill(xc2, yc2, rwyellow);
set(c2,'edgecolor', rwyellow);

axis([fxmin fxmax fymin fymax])
daspect([1,1,1])
axis off



 