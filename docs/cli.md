# Command-Line Interface `openborders`

A small toolbox to make open-borders metrics using World Bank (& ILO) data.

**Usage**:

```console
$ openborders [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `empty`: Wipe existing cached information if it...
* `load`: Load data from World Bank & GDIM to be...
* `preprocess`: Preprocess loaded data from World Bank &...
* `reset`: Wipe existing cached information if it...
* `rm`: Wipe existing cached information if it...
* `show`: Show loaded data from World Bank & GDIM to...
* `wipe`: Wipe existing cached information if it...

## Emptying cache `openborders empty`

Wipe existing cached information if it exists. Alias for `reset`.

**Usage**:

```console
$ openborders empty [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### Aliases

* `opbd rm`
* `opbd reset`
* `opbd wipe`

## `openborders load`

Load data from World Bank & GDIM to be used subsequently.

**Usage**:

```console
$ openborders load [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `openborders preprocess`

Preprocess loaded data from World Bank & GDIM to be used subsequently.

**Usage**:

```console
$ openborders preprocess [OPTIONS]
```

**Options**:

* `-i, --indicator TEXT`: Filter the view on an indicator
* `-li, --list-indicators`: List available indicators
* `-ygt, --year-greater INTEGER`: Whether to filter on years greater than {value}  [default: 1980]
* `-dna, --drop-na`: Whether to drop NA values.
* `-n, --norm`: Whether to scale every metric to [0,1] using the per-country
* `-o, --outfile TEXT`: Output the result as a flat file. (Formats: .csv, .xlsx, .json)
* `-d, --debug`: Debug using log statements at each inner loop operation.
* `--help`: Show this message and exit.



## `openborders show`

Show loaded data from World Bank & GDIM to be used subsequently.

**Usage**:

```console
$ openborders show [OPTIONS]
```

**Options**:

* `-i, --indicator TEXT`: Filter the view on an indicator
* `-li, --list-indicators`: List available indicators
* `-pp, --pre-process`: Whether to preprocess the raw cache data & display the results of the aggregation instead.
* `-ygt, --year-greater INTEGER`: Whether to filter on years greater than {value}  [default: 1990]
* `-o, --outfile TEXT`: Output the result as a flat file. (Formats: .csv, .xlsx, .json)
* `-d, --desc`: Add description column to the resulting table.
* `--help`: Show this message and exit.

## `openborders wipe`

Wipe existing cached information if it exists. Alias for `reset`.

**Usage**:

```console
$ openborders wipe [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

