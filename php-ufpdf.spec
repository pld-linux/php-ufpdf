%define	sver	%(echo %{version} | tr -d .)
Summary:	PHP class which allows to generate PDF files with pure PHP
Summary(pl.UTF-8):	Klasa PHP pozwalająca na generowanie plikow PDF w czystym PHP
Name:		php-ufpdf
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.acko.net/files/ufpdf.zip
# Source0-md5:	1ae3792810334c15dcec3773b4d5bf54
# http://www.fpdf.de/downloads/addons/69/
Source1:	ufpdf-draw.php
# Source1-md5:	c8ff16105021bb1edc2023a3c9e4be19
URL:		http://acko.net/node/56
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php(core)
Requires:	php-fpdf
Obsoletes:	ufpdf < 0.1-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FPDF is a PHP class which allows to generate PDF files with pure PHP,
that is to say without using the PDFlib library. F from FPDF stands
for Free: you may use it for any kind of usage and modify it to suit
your needs.

UFPDF, an extension of FPDF which accepts input in UTF-8.

%description -l pl.UTF-8
FPDF to klasa PHP pozwalająca na generowanie plików PDF w czystym PHP,
tzn. bez użycia biblioteki PDFlib. F z FPDF oznacza "Free": można jej
używać w dowolny sposób i modyfikować w zależności od potrzeb.

UFPDF, rozszerzenie FPDF pozwalające na akceptowanie danych
wejściowych w UTF-8.

%prep
%setup -q -n %{name}

sed -i -e 's#fpdf.php#fpdf/fpdf.php#g' ufpdf.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/ufpdf
cp -p ufpdf.php $RPM_BUILD_ROOT%{php_data_dir}/ufpdf/ufpdf.php
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{php_data_dir}/ufpdf/udraw.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt ufpdf-test.php tools/*.php
%{php_data_dir}/ufpdf
