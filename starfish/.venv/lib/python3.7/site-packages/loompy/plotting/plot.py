import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from sklearn.preprocessing import LabelEncoder
from typing import *
from ..loompy import LoomConnection
from .color import cat_colors
import logging
import numpy as np


class Variable:
	def __init__(self, ds: LoomConnection, *, transposed: bool, values_by: Union[str, np.ndarray], labels_by: Union[str, np.ndarra] = None, group_by: Variable = None, ndims: int = 1, layer: str = "") -> None:
		self.ds = ds
		self.length = ds.shape[0] if transposed else ds.shape[1]
		self.transposed = transposed
		self.group_by = group_by
		self.values_by = values_by.split(":")[0]
		if self.values_by.startswith("@"):
			self.categorical = True
			self.values_by = self.values_by[1:]
		self.labels_by = labels_by
		self.ndims = ndims
		self.layer = layer

		self.values = self._get_values(values_by, layer)
		self.labels = None if labels_by is None else self._get_values(labels_by, layer)

	def _get_values(self, values_by: Union[str, np.ndarray], layer: str) -> np.ndarray:
		ds = self.ds
		if self.transposed:
			if isinstance(values_by, np.ndarray):
				if values_by.shape[0] != ds.shape[0]:
					raise ValueError("Array length must match number of rows in file")
				if values_by.ndim != self.ndims:
					raise ValueError(f"Array must have {self.ndims} dimensions, but has {values_by.ndim} dimensions")
				return values_by
			if values_by in ds.ra:
				return ds.ra[values_by]
			for attr in ds.ca.keys():
				if values_by in ds.ca[attr]:
					return ds[layer][:, ds.ca[attr] == values_by][0]
		else:
			if isinstance(values_by, np.ndarray):
				if values_by.shape[0] != ds.shape[1]:
					raise ValueError("Array length must match number of rows in file")
				if values_by.ndim != self.ndims:
					raise ValueError(f"Array must have {self.ndims} dimensions, but has {values_by.ndim} dimensions")
				return values_by
			if values_by in ds.ca:
				return ds.ca[values_by]
			if "Gene" in ds.ra and values_by in ds.ra.Gene:
				return ds[layer][ds.ra.Gene == values_by, :][0]
			for attr in ds.ra.keys():
				if values_by in ds.ra[attr]:
					return ds[layer][ds.ra[attr] == values_by, :][0]
			raise ValueError(f"'{values_by}' not found in file")


class Plot:
	def __init__(self, ds: LoomConnection, size: Tuple[float, float] = None, shape: Tuple[int, int] = (1, 1)) -> None:
		self.ds = ds
		if size is None:
			self.w = shape[1] * 6.0
			self.h = shape[0] * 6.0
		else:
			self.w = size[0]
			self.h = size[1]
		self.n_rows = shape[0]
		self.n_cols = shape[1]

		self.loc = (0, 0)
		plt.figure(figsize=(self.w, self.h))
		plt.subplots_adjust(hspace=0.1, wspace=0.1)

	def scatter(
		self,
		*,
		xy: str = "TSNE",
		color_by: Union[str, Tuple[str, str]] = None,
		size_by: Union[str, Tuple[str, str]] = None,
		zi: bool = True,
		size: float = 10,
		cmap: str = "viridis",
		show_axes: bool = False,
		span: int = 1,
		axis_labels: Union[Tuple, str, bool] = "auto",
		layer: str = "",
		transposed: bool = False) -> None:

		if isinstance(xy, tuple):
			x = Variable(self.ds, transposed=transposed, layer=layer, values_by=xy[0], ndims=1).values
			y = Variable(self.ds, transposed=transposed, layer=layer, values_by=xy[1], ndims=1).values
			if axis_labels == "auto":
				axis_labels = (xy[0], xy[1])
		else:
			var = Variable(self.ds, values_by=xy, ndims=2, layer=layer, transposed=transposed)
			x = var.values[:, 0]
			y = var.values[:, 1]
			if axis_labels == "auto":
				axis_labels = False

		if self.loc[0] >= self.n_rows:
			raise ValueError(f"Too many panels for layout of {self.n_rows} rows and {self.n_cols} columns.")
		ax = plt.subplot2grid((self.n_rows, self.n_cols), self.loc, rowspan=span)
		col = self.loc[1] + span
		row = self.loc[0]
		if col >= self.n_cols:
			col = 0
			row = row + 1
		self.loc = (row, col)

		if size_by is not None:
			if isinstance(size_by, tuple):
				size_var = Variable(self.ds, values_by=size_by[0], labels_by=size_by[1], layer=layer, transposed=transposed)
			else:
				size_var = Variable(self.ds, values_by=size_by, labels_by=size_by, layer=layer, transposed=transposed)
			size_data = size * size_var.values
		else:
			size_data = size
		if not show_axes:
			plt.axis("off")
		if zi:
			plt.scatter(x, y, s=size_data, c='lightgrey', lw=0)
		if isinstance(axis_labels, tuple):
			plt.xlabel(axis_labels[0])
			plt.ylabel(axis_labels[1])

		# Color
		if color_by is not None:
			if isinstance(color_by, tuple):
				color_var = Variable(self.ds, values_by=color_by[0], labels_by=color_by[1], layer=layer, transposed=transposed)
			else:
				color_var = Variable(self.ds, values_by=color_by, labels_by=color_by, layer=layer, transposed=transposed)
			color_data = color_var.values
			color_labels = color_var.labels

			if color_var.categorical:
				color_encoder = LabelEncoder().fit(color_data)
				color_data = color_encoder.transform(color_data)

				uniques = np.unique(color_data)
				n_uniques = len(uniques)
				cc = cat_colors(len(uniques))
				for ix, lbl in enumerate(uniques):
					cols = (color_data == lbl)
					plt.scatter(x[cols], y[cols], s=size_data[cols], c=cc[ix], lw=0, label=lbl)
				if color_labels is not None:
					plt.legend()
			else:
				if zi:
					cols = (color_data > 0)
					plt.scatter(x[cols], y[cols], s=size_data[cols], c=color_data[cols], cmap=cmap, lw=0)
				else:
					plt.scatter(x, y, s=size_data, c=color_data, cmap=cmap, lw=0)
				if color_labels is not None:
					cbaxes = inset_axes(ax, width="30%", height="5%", loc=2)
					cbar = plt.colorbar(cax=cbaxes, orientation='horizontal')
					cbar.set_label(color_by)
