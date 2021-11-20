import { Component, OnInit, Output,EventEmitter, Input } from '@angular/core';
import { APIClientService, getPlaylistResponse } from '../apiclient/apiclient.service';


export interface trackItem
{
  artist:string
  track:string
  album_image_url:string
  preview_url:string|null
}


@Component({
  selector: 'app-searchbox',
  templateUrl: './searchbox.component.html',
  styleUrls: ['./searchbox.component.scss']
})
export class SearchboxComponent{
  @Input()
  searchQuery:string = ""
  tracks:trackItem[] = [];
  
  requestState = "idle"

  constructor(private apiClient:APIClientService) {
   }

  onSearchClicked()
  {
    this.tracks = []
    this.requestState = "loading"
    this.apiClient.getPlaylist(this.searchQuery).subscribe( response => {
      this.tracks = response.data ?? []
      
    },
    (error) => {
      this.requestState = "error"
    },
    () => {
      if(this.tracks.length ==0)
      this.requestState = "error"
      else 
      this.requestState = "idle"
    }

    )
  }

  onSearchChanged(event:any)
  {
    this.searchQuery = event.target.value;
  }

  clearSearch()
  {
    this.searchQuery = "";
    this.tracks = [];
    this.requestState = "idle";
  }
}
